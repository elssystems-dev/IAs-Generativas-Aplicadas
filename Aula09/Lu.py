# Automação de
import cv2
import pyautogui as pt

# Visão computacional
import cv2 as cv

# Manipulação de caminhos no Windows
from pathlib import Path

# Agente de IA - Agno
from agno.media import Image
from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

def automation(dedos:str):
    match dedos:
        case "1":
            print("Um dedo levantado")
            auto1()
        case "2":
            print("Dois dedos levantados")
            auto2()
        case "3":
            print("Três dedos levantados")
        case "4":
            print("Quatro dedos levantados")
        case "5":
            print("Cinco dedos levantados")
        case _:
            print("Nenhum dedo levantado ou mais de cinco dedos levantados")

def auto1():
    pt.press("win")
    pt.write("google")
    pt.press("enter")
    pt.sleep(2)
    pt.write("SENAI american")
    pt.press("enter")

def auto2():
    pt.press("win")
    pt.write("word")
    pt.press("enter")

camera = cv2.VideoCapture(0)

if camera.isOpened():
    validacao, frame = camera.read()
    while validacao:
        validacao, frame = camera.read()
        imagemCriada = cv.flip(frame[:,:,:3], 1)
        regiao = cv.rectangle(imagemCriada, (240, 140), (420, 340), (0, 0, 255), 3)
        cv.imshow("Câmera de pesquisa", regiao)
        tecla = cv.waitKey(5)
        if tecla == 27:
            break
    cv.imwrite("SENAIPESQUISA.png", regiao)
camera.release()
cv.destroyAllWindows()

caminho = Path("SENAIPESQUISA.png")

agentImagem = Agent(
    model=OpenAIResponses(
        id="gpt-5.2",
        api_key = API_KEY
    ),
    instructions= "Você é um agente de visão computacional que só reconhece as mãos de pessoas que estão dentro do retângulo vermelho. Você deve analisar a imagem e responder quantos dedos levantados a pessoa está. REGRAS: -Não escrever sobre os demais objetos que não sejam dedos; - Somente falar quantos dedos estão levantados sem mais detalhes; - Responder apenas com um número inteiro",
    tools=[automation],
    markdown=True
)

ImagemToByte = caminho.read_bytes()
agentImagem.run("Me fale sobre esta imagem",
    images=[Image(content=ImagemToByte)],)