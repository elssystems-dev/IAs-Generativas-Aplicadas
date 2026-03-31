from openai import OpenAI
from pathlib import Path

from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

cliente = OpenAI(api_key=API_KEY)

audio_caminho = Path(__file__).with_name("resposta.mp3")

with audio_caminho.open(mode="rb") as audio:
    transcricao = cliente.audio.transcriptions.create(
        model="whisper-1",
        file=audio
    )

print(transcricao)