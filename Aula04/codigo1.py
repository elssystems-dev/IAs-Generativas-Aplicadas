# Importar os frameworks

from openai import OpenAI

from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

cliente = OpenAI(api_key=API_KEY)

ENTRADA = "Escreva um código em python no qual tenha que verificar se um número é primo, este número será digitado pelo usuário."

resposta = cliente.responses.create(
    model="gpt-4", #Modelo LLM
    input=ENTRADA,
    instructions=  "Você é um pirata que fala como pirata"
                    "escreve como pirata e pensa como pirata, "
                    "responda a pergunta do usuário como um pirata."
                    "REGRAS:"
                    "Sempre que o usuário pedir código em python, "
                    "responda com um código em python, "
                    "não responda nada além do código. "
)

print(resposta.output_text)