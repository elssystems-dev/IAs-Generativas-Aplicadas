# Automação de teclado e mouse
import cv2
import pyautogui as pi

# Path
from pathlib import Path as pt

# OpenCV
import cv2 as cv

# Agno
from agno.media import Image
from agno.agent import Agent
from agno.models.openai import OpenAIResponses

from pathlib import Path

from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

webcam99 = cv.VideoCapture(0)

if webcam99.isOpened():
    validacao, frame = webcam99.read()
    while validacao:
        validacao, frame = webcam99.read()
        imagemWeb = cv.flip(frame[:,:,:3], 1)
        roi = cv.rectangle(imagemWeb, (100,100), (240, 240), (0,0,255), 3)
        cv.imshow("Webcam", roi)
        tecla = cv.waitKey(5)
        if tecla == 27:
            break
    cv.imwrite("SENAI.png", roi)
webcam99.release()
cv.destroyAllWindows()
