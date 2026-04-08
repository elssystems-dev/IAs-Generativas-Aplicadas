# Langchain
from langchain.agents import create_agent
from langchain_community.utilities import SQLDatabase
from langchain_core.tools import tool
from langgraph.runtime import get_runtime

# OS - Sistema Operacional
import os
from dotenv import load_dotenv

# Dataclass - Cria classes para armazenar dados
from dataclasses import dataclass

# Ipython - Image display
from IPython.display import Image, display

from REVISAO import resultado

db_path = os.path.abspath("chinook.db")
db = SQLDatabase.from_uri(f"sqlite:///{db_path.replace('\\', '/')}")

@dataclass
class ContextoDeTempoDeExecucao:
    db: SQLDatabase

@tool
def execute_sql(query:str) -> str:
    runtime = get_runtime(ContextoDeTempoDeExecucao())
    db = runtime.context.db
    try:
        resultado = db.run(query)
        return resultado
    except Exception as e:
        return f"Erro ao executar query: {str(e)}"

load_dotenv()
API_KEY = os.getenv("API_KEY")

os.environ["OPENAI_API_KEY"] = API_KEY

PROMPT_SISTEMA = '''
Você é uma analista de banco de dados SQL

REGRAS:
- Pense passo a passo;
- Quando precisar de dados, chame a ferramente 'execute-sql' com ONE SELECT query;
- Somente Read-Only, não faça INSERT, UDATE, DELETE, ALTER, DROP, CREATE, REPLACE e TRUNCATE;
- LImite de 5 linhas para saída a não ser que o usuário peça por mais;
- Se a ferramenta retornar m erro, revise o SQL e tente novamente;
- Prefira colnas explícitas ao invés de SELECT * para evitar erros de sintaxe;

'''

agenteLANG = create_agent(
    model="openai:gpt-3.5-turbo",
    tools=[execute_sql],
    system_prompt=PROMPT_SISTEMA,
    context_schema=ContextoDeTempoDeExecucao()
)

pergunta = "Qual a tabela tem mais registros?"

for passos in agenteLANG.stream(
    {"messages": pergunta},
    context=ContextoDeTempoDeExecucao(db=db),
    stream_mode="values",
):
    passos["messages"][-1].pretty_print()