from fastapi import FastAPI
from routes import Router
from routes_documentos import Router_documentos

app = FastAPI()

@app.get("/")
def mensagem():
    return {"mensagem"> "tudo certo!"}

app.include_router(Router)
app.include_router(Router_documentos)

