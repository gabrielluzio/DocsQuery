from google import genai
import os
from dotenv import load_dotenv

def analisar(texto_pdf, pergunta_usuario):
        load_dotenv()
        try:
            Cliente =  genai.Client(api_key=os.getenv('API_GEMINI'))
            prompt = f"- Utilize linguagem natural, clara e humanizada, converse com o usuário como um assistente, não como um relatório,evite expressões robóticas, seja objetivo e responda diretamente à pergunta, organize as informações quando necessário, sem exagerar em listas, Não invente informações que não estejam presentes no documento, Preserve a precisão das informações extraídas com base nesse arquivo:\n{texto_pdf}\n\nResponda:\n{ pergunta_usuario}:"
            resposta = Cliente.models.generate_content(
                model='gemini-3.5-flash-lite',
                contents=prompt
            )
            return resposta.text
        except Exception:
            raise Exception("Erro ao analisar documento.")