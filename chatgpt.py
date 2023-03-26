import openai
import os
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("API_KEY")
MODEL_ID = "gpt-3.5-turbo"

def chatgpt_conversation(conversation):
    response = openai.ChatCompletion.create(
        model = MODEL_ID,
        messages = conversation
    )
    conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    return conversation

if __name__ == '__main__':
    test = chatgpt_conversation([{'role': 'user', 'content':"Hola, como estas?"}])
    print(test[-1]['content'])