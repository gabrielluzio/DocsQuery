from fastapi import APIRouter
from schemas import cadastro, login
from fastapi import Depends
from sqlalchemy.orm import Session
from database import get_db
from models import usuarios
from security import gerar_hash, verificar_hash
from fastapi import HTTPException
from argon2.exceptions import VerifyMismatchError

Router = APIRouter(prefix = "/auth", tags = ["/auth"]) 

@Router.post("/cadastr")
#rota para usuario fazer cadastro.
def rota_cadastro(pycadastro: cadastro, db: Session = Depends(get_db)):
     cadastro_usuario = usuarios(
          nome = pycadastro.nome,
          email = pycadastro.email,
          senha = gerar_hash(pycadastro.senha)
     )
     db.add(cadastro_usuario)
     db.commit()
     return{"mensagem": "usuario cadastrado. "}
   


@Router.post("/login")
#rota para usuario fazer login.
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
     
     return {"mensagem": "Login realizado com sucesso"}

    