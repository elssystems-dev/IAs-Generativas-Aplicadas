# Importações dos módulos p/ o APP
import streamlit as st # UI Web
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb

# Configurações da página Web
st.set_page_config(
    page_title="Agente IA com Memória",
    layout="wide",
    page_icon="🤖"
)

st.title("🤖 Agente de IA com memória - Aula 06 🤖")
st.markdown("Conversa com um Agente de IA")
from dotenv import load_dotenv
import os

load_dotenv()
API = os.getenv("API_KEY")

# Iniciar o agente na sessão web
if "agente" not in st.session_state:
    st.session_state.agente = Agent(
        model=OpenAIChat(
            id= "gpt-3.5-turbo",
            api_key=API
        ),
        db = SqliteDb(db_file="agente.db"),
        add_history_to_context=True,
        num_history_runs=3,
        markdown=True
    )

# Iniciar o histórico de conversas
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir o histórico de conversas
st.subheader("Histórico de Conversas")
chat_container = st.container()

with chat_container:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Entrada do usuário
entrada_user = st.chat_input("Digite sua mensagem aqui...")

if entrada_user:
    # Adicionar mensagem do usuário ao histórico
    st.session_state.messages.append({
        "role": "user",
        "content": entrada_user
    })

    # Exibir a mensagem do usuário
    with chat_container:
        with st.chat_message("user"):
            st.markdown(entrada_user)

    # Gerar a resposta do agente
    with st.spinner("agente de IA pensando..."):
        try:
            resposta = st.session_state.agente.run(entrada_user, session_id="1")
            resposta_texto = resposta.content if hasattr(resposta, "content") else str(resposta)

            # Adicionar a resposta do agente ao histórico
            st.session_state.messages.append({
                "role": "assistant",
                "content": resposta_texto
            })

            # Exibir resposta do agente
            with chat_container:
                with st.chat_message("assistant"):
                    st.markdown(resposta_texto)

        except Exception as e:
            st.error(f"Erro ao processar a solicitação: {str(e)}")

#Sidebar com as informações do agente e botões

with st.sidebar:
    st.title("Configurações")

    if st.button("Limpar conversa 🧼"):
        st.session_state.messages = []
        st.rerun()
    st.divider()
    st.info(
        """
        Este agente utiliza:
        Modelo: GPT-3.5 Turbo
        Banco de dados: SQLite
        Memória: Últimas 3 interações
        """
    )
    st.divider()
    st.caption(f"Total de mensagens: {len(st.session_state.messages)}")