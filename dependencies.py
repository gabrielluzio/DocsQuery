from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jwt_handler import validar_tokens


bearer = HTTPBearer()

def obter_usuario_id(
    credenciais: Annotated[
        HTTPAuthorizationCredentials,
        Depends(bearer)
    ]
):

    payload = validar_tokens(credenciais.credentials)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado",
            headers={"WWW-Authenticate": "Bearer"}
        )

    try:
        usuario_id = int(payload["sub"])

        if usuario_id <= 0:
            raise ValueError

    except (ValueError, TypeError, KeyError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Identificador de usuário inválido",
            headers={"WWW-Authenticate": "Bearer"}
        )

    return usuario_id
    