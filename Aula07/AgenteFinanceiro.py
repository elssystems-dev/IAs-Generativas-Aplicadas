from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

agenteFinanceiroSenai = Agent(
    model = OpenAIChat(
        id="gpt-3.5-turbo",
        api_key=API_KEY),
        tools = [
            YFinanceTools(
                enable_stock_price=True, #Busca preço de ações
                enable_analyst_recommendations=True,
                enable_company_info=True,
                enable_stock_fundamentals=True
            )
        ],
    description="Você é um analista de investimento que pesqusia preços de ações no mercado brasileiro, traz recomendações de analistas e sobre as empresas que o usuário vai investir.",
    instructions="Formate sua resposta usando Markdown e utilize tabelas para exibir os dados sempre que possível"
)

agenteFinanceiroSenai.print_response(
    "Use o yfinance para buscar o preço e recomendações da Petrobrás e depois formate em uma tabela histórico de preço dos últimos registros"
)