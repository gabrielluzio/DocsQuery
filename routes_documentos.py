from fastapi import UploadFile
from fastapi import APIRouter, Depends
from fastapi import  HTTPException
import pymupdf
from dependencies import obter_usuario_id


Router_documentos = APIRouter(prefix= "/documentos", tags=["documentos"], dependencies=[Depends(obter_usuario_id)])

documentos_pdf = {}
@Router_documentos.post("/criar_documentos")
async def upload_file(arquivo: UploadFile):
    
    tamanho_mxm = 10 * 1024 * 1024 # Define o tamanho máximo permitido para o arquivo, em bytes (10 MB).
    tamanho_arquivo = arquivo.size # Obtém o tamanho do arquivo enviado e armazena na variável tamanho_arquivo.
    
    await arquivo.seek(0) # Retorna o cursor de leitura para o início do arquivo, permitindo ler novamente seu conteúdo e verificar se ele possui a assinatura de um PDF.


    # tratamento de erros para verificar se o arquivo e maior que tamanho maximo, e para verificar se o arquivo esta vazio. 
    if arquivo.size is None:
          raise HTTPException(status_code=400, detail="Não foi possível identificar o tamanho do arquivo. ")
    elif tamanho_arquivo > tamanho_mxm:
                raise HTTPException(status_code=413, detail="Conteúdo grande demais. ")

    
    leitura_arquivo = await arquivo.read()# Lê todo o conteúdo do arquivo a partir da posição atual do cursor e armazena os dados em bytes na variável leitura_arquivo.

    # tratamento de erros para arquivo vazio, e para verficar se o arquivo e um PDF valido
    if tamanho_arquivo == 0:
            raise HTTPException(status_code=400, detail="arquivo vazio. ")
    elif not leitura_arquivo.startswith(b"%PDF-"):
        raise HTTPException(status_code=415, detail="Tipo de mídia não suportado. ")


    # Abre o arquivo PDF a partir dos bytes armazenados em 'leitura_arquivo', permitindo acessar suas páginas para extrair o conteúdo posteriormente.
    try:
        documento_aberto_pymu = pymupdf.Document(stream=leitura_arquivo, filetype="pdf")
    except pymupdf.FileDataError:
          raise HTTPException(
          status_code=422,
          detail="O arquivo PDF está corrompido ou é inválido"
    )

    
    #faz o tratamento de erros para arquivo sem texto extraivel, e faz a iteração de cada apgina do documento para extrair conteudo das apginas de forma separada. 
    paginas_pdf = {}
    try:
        for page in documento_aberto_pymu: #Percorre todas as páginas do documento PDF.
            texto_pdf = page.get_text() # 	Extrai o texto da página atual do PDF.
            if not texto_pdf.strip():
                raise HTTPException(
                        status_code=422,
                        detail=f"Pagina {page.number+1} não possui texto extraível"
                )

            #dicionario para facilitar a entrega de conteudo para o GEMINI. 
            documentos_pdf [page.number+1] = texto_pdf
        return documentos_pdf
           
    finally:
        documento_aberto_pymu.close()
    