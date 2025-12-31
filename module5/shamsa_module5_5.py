
import requests

# Ollama Chat API
url = "http://localhost:11434/api/chat"

# System prompt (persona)
system_message = {
    "role": "system",
    "content": "You are a helpful assistant that explains clearly and simply."
}

# User input
user_text = input("Enter your question: ")

user_message = {
    "role": "user",
    "content": user_text
}

# Settings for model behavior
options = {
    "temperature": 0.5 ,   # creativity level
    "num_ctx": 4096       # context window size
}

# Request body

data = {
    "model": "gemma3:1b",
    "messages": [system_message, user_message],
    "options": options,
    "stream": False
}

# Send request
response = requests.post(url, json=data)

# Parse response
result = response.json()

# Output
print("\nOllama says:")
print(result["message"]["content"])


