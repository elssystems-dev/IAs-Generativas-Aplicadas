from agno.agent import Agent
from agno.models.openai import OpenAIChat

from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

agent = Agent(
    model = OpenAIChat(
        id= "gpt-4o-mini",
        api_key=API_KEY,
        instructions= "Você é um pirata que responde perguntas de forma clara e concisa"
                      "com respeito e profissionalismo de um pirata. Tente resumir suas respostas"
    ),
    markdown=True,
)
while True:
    pergunta = input("\nDigite a sua pergunta: ")
    if pergunta.lower() == 'sair':
        break
    agent.print_response(pergunta,stream=True)
