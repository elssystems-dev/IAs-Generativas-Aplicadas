import cv2 #OpenCV

# Agente Agno
from agno.media import Image
from agno.agent import Agent
from agno.models.openai import OpenAIResponses

# Biblioteca Path para manipular caminho e arquivos
from pathlib import Path

from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

objetos1 = ["Garrafa de água", "Garrafa plástica", "Garrafa", "Garrafa térmica"]

def recommendations(objeto:str):
    ok = False
    for obj in range(len(objetos1)):
        print(objetos1[obj])
        if objetos1[obj] == objeto:
            ok = True
    if ok:
        return "Beba mais água"
    return "Não tenho mais recomendações para este objeto"

webcam = cv2.VideoCapture(0)

if webcam.isOpened():
    validacao, frame = webcam.read()
    while validacao:
        validacao, frame = webcam.read()
        imagem = cv2.flip(frame [:,:,:3], 1)
        frameROI = cv2.circle(imagem, (300, 250), 80, (255,0,0), 2, cv2.LINE_AA)
        cv2.imshow("Webcam", frameROI)
        chave = cv2.waitKey(5)
        if chave == 27:
            break
    cv2.imwrite("FotoSENAI.png", frameROI)

webcam.release()
cv2.destroyAllWindows()

caminhoDaImagem = Path("FotoSENAI.png")

agenteROI = Agent (
    model=OpenAIResponses(
        id = "gpt-5.2",
        api_key = API_KEY,
    ),
    instructions= "Vocé é um agente de visão computacional que só reconhece objetos que estão dentro do círculo azul da imagem. Você deve analisar a imagem e responder quaissobjetos estão dentro do círculo azul. REGRAS: Não escrever sobre os demais objetos que estão fora do círculo azul. Somente falar o que é objeto sem mais detalhes. Somente falar um nome de objeto",
    tools=[],
    markdown=True
)

byImage = caminhoDaImagem.read_bytes()

agenteROI.print_response(
    "Me fale sobre esta imagem",
    image= [Image(content=byImage)]
)