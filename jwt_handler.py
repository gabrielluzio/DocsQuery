import jwt
from datetime import datetime, timedelta, timezone
from jwt.exceptions import InvalidTokenError


#gerar tokens jwt
chave_jwt = "fbc87479a5f7069f6d281fdc663acabf195e6c018e63f718612a37c7887d86b2"
algoritmo_jwt = "HS256"

def gerar_token(usuario_id):

    dados_jwt = {
        "sub": str(usuario_id),
        "exp": datetime.now(timezone.utc) + timedelta(minutes=30)
    }

    tokens_jwt = jwt.encode (
        dados_jwt,
        chave_jwt,
        algorithm = algoritmo_jwt
    )

    return tokens_jwt


#validar tokens 
def validar_tokens(token:str):
    try:
        payload = jwt.decode(
            token,
            chave_jwt,
            algorithms = ["HS256"],
            options = {"require": ["sub", "exp"]}
        )

        return payload
    
    except InvalidTokenError:
        return None
