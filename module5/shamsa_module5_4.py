
import requests

url = "http://localhost:11434/api/chat"

# System prompt (persona)
system_prompt = {
    "role": "system",
    "content": "You are a friendly Python teacher. Explain answers simply and clearly."
}

# Get user input
user_text = input("Enter your question: ")

# User message
user_prompt = {
    "role": "user",
    "content": user_text
}

# Data sent to Ollama
data = {
    "model": "gemma3:1b",
    "messages": [system_prompt, user_prompt],
    "stream": False
}

# Send request
response = requests.post(url, json=data)

# Read response
result = response.json()

# Print AI answer
print("\nAI Response:")
print(result["message"]["content"])

