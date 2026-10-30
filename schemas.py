#definem e validam os dados que entram e saem da API, geralmente usando Pydantic.
from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Annotated
import re

class cadastro(BaseModel):
    nome: str
    email: EmailStr
    senha: Annotated[str, Field(minlength=8, maxlength=12)]

    @field_validator("nome") 
    @classmethod
    def validar_nome(cls, value_nome):# funçao para validar regras no nome.
        if not value_nome.strip():
            raise ValueError("nome nao pode estar vazio.")
        elif len(value_nome) < 3 or len(value_nome) > 30 :
                    raise ValueError("nome muito curto ou muito longo, minimo de 3 caracteres e maximo de 30 caracteres.")
        elif not re.fullmatch(r"[A-Za-zÀ-ÿ ]+", value_nome):
              raise ValueError("nome nao pode conter caracteres especiais. ")
        return value_nome.strip()



class login(BaseModel):
    email:EmailStr
    senha: Annotated[str, Field(minlength=8)]