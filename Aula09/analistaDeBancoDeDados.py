#Langchain
from langchain.agents import create_agent
from langchain_community.utilities import SQLDatabase
from langchain_core.tools import tool
from langgraph.runtime import get_runtime

#OS - Sistema Operacional
from pathlib import Path
from zipfile import ZipFile

#Dataclass - Cria classes para armazenar dados
from dataclasses import dataclass

from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

BASE_DIR = Path(__file__).resolve().parent

def resolver_caminho_banco(base_dir: Path) -> Path:
    db_path = base_dir / "chinook.db"
    sqlite_path = base_dir / "Chinook_Sqlite.sqlite"
    zip_path = base_dir / "data.zip"

    # Se chinook.db existir mas estiver vazio, tenta recuperar do zip de dados.
    if db_path.exists() and db_path.stat().st_size == 0 and zip_path.exists():
        with ZipFile(zip_path, "r") as arquivo_zip:
            if "Chinook_Sqlite.sqlite" in arquivo_zip.namelist():
                arquivo_zip.extract("Chinook_Sqlite.sqlite", path=base_dir)

    for candidato in (db_path, sqlite_path):
        if candidato.exists() and candidato.stat().st_size > 0:
            return candidato

    raise FileNotFoundError(
        "Banco de dados não encontrado ou vazio. "
        f"Esperado: {db_path} ou {sqlite_path}"
    )


db_path = resolver_caminho_banco(BASE_DIR)

db = SQLDatabase.from_uri(f"sqlite:///{db_path.as_posix()}")
tabelas_disponiveis = ", ".join(sorted(db.get_usable_table_names()))

#Define o contexto de tempo de execução p/ a tool
@dataclass
class ContextoDeTempoDeExecucao:
    db: SQLDatabase

#Definir a ferramenta de execução do SQL
@tool
def execute_sql(query:str) -> str:
    """Executa uma consulta SQL read-only no banco configurado e retorna o resultado em texto."""
    runtime = get_runtime(ContextoDeTempoDeExecucao)
    db = runtime.context.db
    try:
        resultado = db.run(query)
        return resultado
    except Exception as e:
        return f"Erro ao executar a query: {str(e)}"

PROMPT_SISTEMA = f'''
Você é um analista de banco de dados SQL

REGRAS:
- Pense passo a passo;
- Quando precisar de dados, chame a ferramenta 'execute_sql' com ONE SELECT query;
- Somente Read-Only, não faça INSERT, UPDATE, DELETE, ALTER, DROP, CREATE, REPLACE e TRUNCATE;
- Limite de 5 linhas para saída a não ser que o usuário peça por mais;
- Se a ferramenta retornar um erro, revise o SQL e tente novamente;
- Prefira colunas explicitas ao invés de SELECT * para evitar erros de sintaxe;
- Antes de consultar dados de negocio, verifique nomes de tabelas/colunas com sqlite_master e PRAGMA table_info;
- Tabelas disponiveis neste banco: {tabelas_disponiveis}
'''

agenteLANG = create_agent(
    model="openai:gpt-3.5-turbo",
    tools=[execute_sql],
    system_prompt=PROMPT_SISTEMA,
    context_schema=ContextoDeTempoDeExecucao,
)

pergunta = "Qual o álbum mais conhecido?"

for passos in agenteLANG.stream(
        {"messages": pergunta},
    context=ContextoDeTempoDeExecucao(db=db),
    stream_mode="values",
):
    passos["messages"][-1].pretty_print()