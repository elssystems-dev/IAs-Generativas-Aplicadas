from openai import OpenAI # Importação da biblioteca OpenAI

from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

cliente = OpenAI(api_key= API_KEY)

emb = cliente.embeddings.create(
    model="text-embedding-3-small",
    input="O que é inteligência artificial?"
)

print(emb.data[0].embedding)