# Importações dos módulos para o APP
import streamlit as st
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.db.sqlite import SqliteDb

from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

# Configurações da página Web
st.set_page_config(
    page_title="Agente IA com Memória",
    layout="wide",
    page_icon="🤖"
)

########### Funções ###########

def iniciar_agente():
    API = os.getenv("API_KEY")

    return Agent(
        model=OpenAIChat(id="gpt-3.5-turbo", api_key=API),
        db=SqliteDb(db_file="agente.db"),
        add_history_to_context=True,
        num_history_runs=3,
        markdown=True
    )

########### Interface do Streamlit ###########

# Título e introdução
st.title("🤖 Agente de IA com memória - Aula 06 🤖")
st.markdown("Conversa com um Agente de IA")

# Opções da sidebar
st.sidebar.title("Opções do Agente")
opcao_atual = st.sidebar.radio("Selecione uma opção:", ("Nova Conversa", "Revisar Conversas Anteriores"))

# Iniciar o agente na sessão web
if "agente" not in st.session_state:
    st.session_state.agente = iniciar_agente()

# Nova conversa
if opcao_atual == "Nova Conversa":
    st.subheader("Nova Conversa")

    # Iniciar o histórico de conversas
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Exibir o histórico de conversas
    chat_container = st.container()
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Entrada do usuário
    entrada_user = st.chat_input("Digite sua mensagem aqui...")

    # Processar a entrada do usuário
    if entrada_user:
        st.session_state.messages.append({"role": "user", "content": entrada_user})

        with chat_container:
            with st.chat_message("user"):
                st.markdown(entrada_user)

        with st.spinner("Agente de IA pensando..."):
            try:
                resposta = st.session_state.agente.run(entrada_user, session_id="1")
                resposta_texto = resposta.content if hasattr(resposta, "content") else str(resposta)
                st.session_state.messages.append({"role": "assistant", "content": resposta_texto})

                with chat_container:
                    with st.chat_message("assistant"):
                        st.markdown(resposta_texto)

            except Exception as e:
                st.error(f"Erro ao processar a solicitação: {str(e)}")

# Revisar conversas anteriores
elif opcao_atual == "Revisar Conversas Anteriores":
    st.subheader("Revisar Conversas Anteriores")

    if "all_messages" not in st.session_state:
        st.session_state.all_messages = {}

    for key, value in st.session_state.all_messages.items():
        st.write(f"Chat ID: {key}")
        for message in value:
            with st.expander("Ver mensagem"):
                st.write(f"{message['role']}: {message['content']}")