import streamlit as st
from openai import OpenAI
import codigo1 as cd

cliente = OpenAI(api_key=cd.API_KEY)

st.title("Chatbot SENAI")
st.text("Digite para a IA abaixo: ")
entrada = st.text_input("Seu prompt:")

if entrada:
    st.text("Resposta da IA")
    resposta = cliente.responses.create(
        model="gpt-4",  # Modelo LLM
        input= entrada,
        instructions="Você é um pirata que fala como pirata"
                     "escreve como pirata e pensa como pirata, "
                     "responda a pergunta do usuário como um pirata.")
    st.text(resposta.output_text)