import json
from flask import Flask, request, jsonify
import openai
from chatbot import gpt3, append_interaction_to_chatlog
from TextSpeech import text_to_speech
from SpeechText import get_audio

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def hello_world():
    return 'This is a test...'

@app.route('/getresponse', methods=["POST"])
def voicebot_response(speech_input):
    
    text_input = get_audio(speech_input)
    print(type(text_input))

    openAI_response = gpt3(text_input)
    print(openAI_response)

    append_interaction_to_chatlog(openAI_response)
    speech_output = text_to_speech(openAI_response)

    return speech_output

