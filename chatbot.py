import os
from requests import session
import openai
from dotenv import load_dotenv

#openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key ="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"
load_dotenv()


start_sequence = "AI"
restart_sequence = "You"
session_prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly."


chat_log = None

def gpt3(stext, chat_log=None):

    if chat_log is None:
        chat_log = session_prompt

    prompt_text = f'{chat_log}{restart_sequence}: {stext}{start_sequence}:'

    response = openai.Completion.create(
        engine="text-davinci-002", #which gpt engine to use
        prompt=prompt_text, #input text
        temperature=0.5, #number between 0 and 1 that determines how many creative risks the engine takes
        max_tokens=30, #maximum completion length (length of reply)
        top_p=1, #alternative way to control the originality and creativity of generated text
        frequency_penalty=0.5, #number between 0 and 1. The higher the number, the less likely the model repeats itself
        presence_penalty=0 #number between 0 and 1. The higher the number the more likely that gpt will talk about new topics
    )

    reply = str(response.choices[0].text)
    return reply


def append_interaction_to_chatlog(stext, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {stext}{start_sequence}{answer}'



