import streamlit as st
import os
from audio_recorder_streamlit import audio_recorder
from streamlit_float import *
from utils import initialize_session_state, text_to_speech, speech_to_text, get_answer, autoplay_audio

# Float feature initialization
float_init()

# Initialize the session state
initialize_session_state()

st.title("🗣️ Voice Bot using OpenAI")
st.set_page_config(page_title="Voice Bot using Openai", page_icon="🤖")

# Create footer container for the microphone
footer_container = st.container()
with footer_container:
    audio_bytes = audio_recorder(icon_size="2x")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


if audio_bytes:
    # Write audio bytes to file
    with st.spinner("Transcribing..."):
        webm_file_path = "temp_audio.mp3"
        with open(webm_file_path, "wb") as f:
            f.write(audio_bytes)
        # st.audio(audio_bytes, format="audio/mp3")

        transcipt = speech_to_text(webm_file_path)
        if transcipt:
            st.session_state.messages.append({"role":"user","content":transcipt})
            with st.chat_message("user"):
                st.write(transcipt)
            os.remove(webm_file_path)
        

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking🤔..."):
            final_response=get_answer(st.session_state.messages)
        with st.spinner("Generating audio response..."):
            audio_file = text_to_speech(final_response)
            autoplay_audio(audio_file)
        st.write(final_response)
        st.session_state.messages.append({"role":"assistant","content":final_response})
        os.remove(audio_file)

# Float the footer container and provide CSS to target it with
footer_container.float("bottom: 2rem;")
