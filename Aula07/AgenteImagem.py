from agno.agent import Agent
from agno.models.openai import OpenAIResponses
from agno.media import Image
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

imagePath = Path("rj.jpg")

agenteIm = Agent (
    model = OpenAIResponses(
        id="gpt-5.2",
        api_key=API_KEY
    ),
    markdown=True,
)

imageBytes = imagePath.read_bytes()
agenteIm.print_response(
    input = "Me fale sobre esta imagem",
    images = [Image(content=imageBytes)],
)
