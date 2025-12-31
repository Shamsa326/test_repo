
import streamlit as st
import requests

# Title
st.title("Simple LLM Chat (Ollama)")

# User input box
question = st.text_input("Enter your question:")

# Button
ask = st.button("Ask")


# Ollama API
url = "http://localhost:11434/api/chat"

if ask and question:

    data = {
        "model": "gemma3:1b",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant. Answer simply."
            },
            {
                "role": "user",
                "content": question
            }
        ],
        "options": {
            "temperature": 0.7,
            "num_ctx": 4096
        },
        "stream": False
    }

    response = requests.post(url, json=data)
    result = response.json()

    st.write("Answer:")
    st.write(result["message"]["content"])

# install in venv:
# pip install streamlit 

#Run in terminal:
# streamlit run shamsa_module5_6.py

