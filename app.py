import json
from flask import Flask, request, jsonify
from chatbot import gpt3, append_interaction_to_chatlog
from TextSpeech import text_to_speech
from SpeechText import speech_to_text

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def hello_world():
    return 'This is a test...'

@app.route('/getresponse', methods=["POST"])
def voicebot_response(speech_input):
    
    text_input = speech_to_text(speech_input)

    openAI_response = gpt3(text_input)

    speech_output = text_to_speech(openAI_response)

    return speech_output

