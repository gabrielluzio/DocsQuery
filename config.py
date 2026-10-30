#armazena as configurações da aplicação, como variáveis de ambiente, URLs e chaves de API.
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_config = os.getenv("DATABASE")