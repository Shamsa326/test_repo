
import requests

# Ollama API address
url = "http://localhost:11434/api/generate"

# Ask user for input
text = input("Enter your question: ")

# Data sent to Ollama
data = {
    "model": "gemma3:1b",
    "prompt": text,
    "stream": False
}

# Send request
response = requests.post(url, json=data)

# Get result
result = response.json()

# Print AI reply
print("\nOllama says:")
print(result["response"])
