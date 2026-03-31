from openai import OpenAI # Framework da OpenAI
import codigo1 as cd

cliente = OpenAI(api_key=cd.API_KEY) # API KEY do OpenAI
entrada = input("Digite o seu texto: ")
resposta = cliente.responses.create(
    model="gpt-4",
    input=entrada,
    instructions= "Imite a narrativa do Candy Cadet de Five Nights at Freddy's Pizzeria Simulator"
)

ia = resposta.output_text

audio = cliente.audio.speech.create(
    model="tts-1",
    voice="ash",
    input=ia
)

audio.stream_to_file("resposta.mp3")