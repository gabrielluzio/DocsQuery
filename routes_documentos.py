from fastapi import UploadFile
from fastapi import APIRouter
from fastapi import  HTTPException
import pymupdf

Router_documentos = APIRouter(prefix= "/documentos", tags=["/documentos"])


@Router_documentos.post("/criar_documentos")
async def upload_file(arquivo: UploadFile):
    """
Recebe e processa arquivos PDF enviados por meio de uma rota da API.

Utiliza a classe UploadFile, do FastAPI, para receber e acessar o
conteúdo do arquivo enviado na requisição.

Em seguida, utiliza a biblioteca PyMuPDF para abrir o documento PDF
a partir dos bytes recebidos, permitindo percorrer suas páginas
individualmente e extrair o conteúdo de cada uma.
    """
    
    tamanho_mxm = 10 * 1024 * 1024 #definindo tamanho de 10 MiB limite
    tamanho_arquivo = arquivo.size #pega o tamanho do arquivo para fazer tratamento de eros
    
    await arquivo.seek(0) #move o cursor de leitura para o inicio do arquivo, para identificar um pdf

    if arquivo.size is None:
          raise HTTPException(status_code=400, detail="Não foi possível identificar o tamanho do arquivo. ")
    elif tamanho_arquivo > tamanho_mxm:
                raise HTTPException(status_code=413, detail="Conteúdo grande demais. ")
    
    leitura_arquivo = await arquivo.read()#define uma leitura do arquivo


    if tamanho_arquivo == 0:
            raise HTTPException(status_code=400, detail="arquivo vazio. ")
    elif not leitura_arquivo.startswith(b"%PDF-"):
        raise HTTPException(status_code=415, detail="Tipo de mídia não suportado. ")
  
    try:
        documento_aberto_pymu = pymupdf.Document(stream=leitura_arquivo, filetype="pdf")
        # Abre o arquivo PDF a partir dos bytes armazenados em 'leitura_arquivo',
        # permitindo acessar suas páginas e extrair o conteúdo posteriormente.
    except pymupdf.FileDataError:
          raise HTTPException(
          status_code=422,
          detail="O arquivo PDF está corrompido ou é inválido"
    )

    paginas_pdf = {}
    try:
        for page in documento_aberto_pymu: #iterar documento aberto
            texto_pdf = page.get_text() # Extrai o conteúdo da página atual do PDF.
            if not texto_pdf.strip():
                raise HTTPException(
                        status_code=422,
                        detail=f"Pagina {page.number+1} não possui texto extraível"
                )

            paginas_pdf [f"paginas {page.number + 1}"] = texto_pdf# Armazena o texto extraído no dicionário, utilizando
                                                                # o número da página como identificador.
    finally:
        documento_aberto_pymu.close()
    
    return paginas_pdf 



      




    



   
