from requests import session
import openai
from dotenv import load_dotenv
import os
openai.api_key = os.getenv("OPEN_API_KEY")
load_dotenv()


start_sequence = "AI"
restart_sequence = "You"
session_prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly."
def gpt3(stext):
    prompt_text = f'{chat_log}{restart_sequence}: {stext}{start_sequence}:'

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt_text,
        temperature=0.5,
        max_tokens=30,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0
    )

    content = str(response.choices[0].text)
    return content


def append_interaction_to_chatlog(stext, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {stext}{start_sequence}{answer}'



