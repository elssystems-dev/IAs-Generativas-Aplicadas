from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb # Permite o uso de Banco de Dados

from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

agente = Agent(
    model=OpenAIChat(
        id="gpt-3.5-turbo",
        api_key=API_KEY
    ),
    db = SqliteDb(db_file="agente.db"),
    add_history_to_context=True,
    num_history_runs=3,
    markdown=True
)

while True:
    entrada = input("\nDigite o texto: ")
    if entrada.lower() == "sair":
        break
    agente.print_response(entrada, session_id="1")


#Primeira interação - Criar o contexto
#agente.print_response("Eu estou trabalhando em um projeto de API no Python", session_id= "1")

#Segunda interação - Reutiliza o contexto da interação anterior
#agente.print_response("Qual é o framework de teste que devo usar nesse contexto?", session_id= "1")

