import speech_recognition as sr
import os
from chatgpt import chatgpt_conversation

conversation = []

# Crear un objeto de reconocimiento de voz
r = sr.Recognizer()
os.environ['PYALSA_DEBUG'] = '0'


# Utilizar el micrófono como fuente de entrada de audio
while True:
    with sr.Microphone() as source:
        print("Di algo...")
        audio = r.listen(source)

    # Utilizar el reconocimiento de voz de Google para convertir el audio en texto
    try:
        text = r.recognize_google(audio, language='es-ES')
        print("Texto reconocido: " + text)
        print("Preguntando a ChatGPT...")
        conversation.append({"role": "user", "content": text})
        response = chatgpt_conversation(conversation)
        print("ChatGPT: " + response[-1]['content'])
    except sr.UnknownValueError:
        print("No se pudo entender lo que dijiste")
        
    except sr.RequestError as e:
        print("Error al solicitar los resultados del servicio de reconocimiento de voz de Google; {0}".format(e))
