from openai import OpenAI
import os
from dotenv import load_dotenv
import base64
import streamlit as st
from openai.helpers import LocalAudioPlayer

# Load the environment variables
load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

client=OpenAI()

def get_answer(messages):
    system_message = [{"role":"system","content":"You are an helpful AI chatbot, that answers questions asked by User."}]
    messages = system_message + messages
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages
    )
    return response.choices[0].message.content

def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages=[
            {"role":"assistant","content":"Hi, How may I assist you?"}
        ]

def speech_to_text(audio_data):
    with open(audio_data, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            response_format="text",
            file=audio_file,
        )
    return transcript


def text_to_speech(text_data):
    webm_file_path = "temp_audio_play.mp3"
    with client.audio.speech.with_streaming_response.create(
        model="tts-1-hd",
        voice="echo",
        input=text_data,
        instructions="Speak confidently but very politely."
    ) as response:
        response.stream_to_file(webm_file_path)
    return webm_file_path

def autoplay_audio(file_path:str):
    with open(file_path, "rb") as f:
        data= f.read()

    bs64 = base64.b64encode(data).decode("utf-8") 
    md = f"""
    <audio autoplay>   
    <source src="data:audio/mp3;base64,{bs64}" type="audio/mp3">
    </audio> 
    """
    st.markdown(md, unsafe_allow_html=True)

    # st.audio(data, format="audio/mp3")