import cv2
from pathlib import Path
from agno.media import Image
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from dotenv import load_dotenv
import os
from agno.db.sqlite import SqliteDb

load_dotenv()
API_KEY = os.getenv("API_KEY")

webcam = cv2.VideoCapture(0)

if webcam.isOpened():
    validacao, frame = webcam.read()
    while validacao:
        validacao, frame = webcam.read()
        cv2.imshow("Webcam", frame)
        bt = cv2.waitKey(5)
        if bt == 27: #Esc
            break
    cv2.imwrite("./webcam.png", frame)

webcam.release()
cv2.destroyAllWindows()

caminhoImagem = Path("webcam.png")

agenteIACamera = Agent (
    model=OpenAIChat(
        id="gpt-5.2",
        api_key=API_KEY
    ),
    markdown=True,
    db = SqliteDb(db_file="agenteIA.db"),
    add_history_to_context=True,
    num_history_runs=3,
    learning=True,
)

byImagem = caminhoImagem.read_bytes()
agenteIACamera.print_response(
    input="Me fala sobre esta imagem",
    images = [Image(content=byImagem)],
    session_id="dev1"
)

for i in range(3):
    entrada = input("\nDigite uma pergunta p/ a IA: ")
    agenteIACamera.print_response(entrada, session_id="dev1")
print("Saindo do Agente")