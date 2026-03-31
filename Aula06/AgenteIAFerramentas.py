from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb
from agno.tools.hackernews import HackerNewsTools

from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

agente = Agent(
    model=OpenAIChat(
        id="gpt-3.5-turbo",
        api_key=API_KEY,
        instructions="Você é um assistente útil que responde perguntas de forma clara e concisa com profissionalismo. REGRAS: - Resumir suas respostas em no máximo três linhas."
    ),
    db=SqliteDb(db_file="agno.db"),
    add_history_to_context=True,
    num_history_runs=3,
    markdown=True,
    tools=[HackerNewsTools()]
)

agente.print_response("Quais são as notícias mais recentes do Hacker News?")