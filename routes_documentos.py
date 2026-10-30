from fastapi import UploadFile
from fastapi import APIRouter
from fastapi import  HTTPException

Router_documentos = APIRouter(prefix= "/documentos", tags=["/documentos"])


@Router_documentos.post("/criar_documentos")
async def upload_file(arquivo: UploadFile):
    tamanho_mxm = 10 * 1024 * 1024 #definindo tamanho de 10 MiB limite

    tamanho_arquivo = arquivo.size
    
    await arquivo.seek(0) #move o cursor de leitura para o inicio do arquivo
    leitura_arquivo = await arquivo.read(5)#define uma leitura dos 5 primeiro bytes do arquivo, para verificar se e um PDF

    if tamanho_arquivo > tamanho_mxm:
            raise HTTPException(status_code=413, detail="Content Too Large")
    elif tamanho_arquivo == 0:
            raise HTTPException(status_code=400, detail="Unsupported Media Type")
    elif leitura_arquivo != b"%PDF-":
        raise HTTPException(status_code=415, detail="Unsupported Media Type")
    else:
        return {"nome arquivo": arquivo.filename}




    



   
