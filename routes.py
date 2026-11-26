from fastapi import APIRouter
from schemas import cadastro, login, pergunta_pydantic
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
from models import usuarios
from security import gerar_hash, verificar_hash
from fastapi import HTTPException
from argon2.exceptions import VerifyMismatchError
from jwt_handler import gerar_token
from service_ia import analisar
from routes_documentos import documentos_pdf
from dependencies import obter_usuario_id


Router = APIRouter(prefix = "/auth", tags = ["/auth"]) 

#rota para usuario fazer cadastro.
@Router.post("/cadastr")
def rota_cadastro(pycadastro: cadastro, db: Session = Depends(get_db)):
     cadastro_usuario = usuarios(
          nome = pycadastro.nome,
          email = pycadastro.email,
          senha = gerar_hash(pycadastro.senha)
     )
     db.add(cadastro_usuario)
     db.commit()
     return{"mensagem": "usuario cadastrado. "}
   

#rota para usuario fazer login.
@Router.post("/login")
def rota_login(pylogin: login, db: Session = Depends(get_db)):
     usuario= db.query(usuarios).filter_by(email=pylogin.email).first()

     if usuario is None:
          raise HTTPException(
        status_code=401,
        detail="E-mail ou senha inválidos"
    )
     try:
        senha_valida = verificar_hash(
            pylogin.senha,
            usuario.senha
        )
         
     except VerifyMismatchError:
        raise HTTPException(
            status_code=401,
            detail="E-mail ou senha inválidos"
        )

     if not senha_valida:
          raise HTTPException(
          status_code=401,
          detail="E-mail ou senha inválidos"
     )

     token = gerar_token(usuario.id)
     return {
     "access_token": token,
     "token_type": "bearer"
     }


@Router.post("/pergunta_usuario", dependencies=[Depends(obter_usuario_id)])
def funcao_pergunta(pergunta_local:pergunta_pydantic):
    pergunta_final = pergunta_local.parametro_pergunta
    resposta = analisar(documentos_pdf, pergunta_final)
    return resposta

  


