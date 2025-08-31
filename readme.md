# 🗣️ Voice Bot using OpenAI
This is a voice-activated chatbot built with Python and Streamlit, showcasing a complete conversational AI flow. Users can speak their queries and receive spoken responses, powered by OpenAI's Whisper, GPT-3.5-Turbo, and TTS models.

<div align="center">

</div>

## ✨ Features

- Speech-to-Text: Converts your voice into text with high accuracy.

- AI-Powered Responses: Generates intelligent, context-aware answers to your questions.

- Text-to-Speech: Delivers natural-sounding, spoken responses from the AI.

- Intuitive UI: A clean and simple chat interface built with Streamlit.

## 🚀 Getting Started

### Prerequisites
Python 3.8+

An OpenAI API key

### Installation
Clone the repository:

git clone [https://github.com/pradnyesh2/Voice-Bot-using-OpenAI.git](https://github.com/pradnyesh2/Voice-Bot-using-OpenAI.git)


### Install the required packages:
pip install -r requirements.txt

Create a .env file in the project's root directory and add your OpenAI API key:

OPENAI_API_KEY="your_api_key_here"

### 🤖 Usage
To run the application, open your terminal and execute the following command:

streamlit run app.py

The application will open in your web browser. Just click the microphone icon to start the conversation!

### 📄 File Structure
app.py: The main Streamlit application that handles the UI and chat flow.

utils.py: Contains utility functions for interacting with the OpenAI API and managing audio.

requirements.txt: A list of all necessary Python libraries.

.env: Your API key.

## 🙏 Contributing
We welcome contributions! Please see our CONTRIBUTING.md file for details on how to get started.