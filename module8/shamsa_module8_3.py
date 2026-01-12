


import requests
from fastmcp import FastMCP


# Create MCP app
mcp = FastMCP("Ollama MCP")

url= "http://localhost:11434/api/generate"


# create mcp tool:
@mcp.tool()
def Ask(question:str):
    # Data sent to Ollama
    data = {
        "model": "llama3.1",
        "prompt": question,
        "stream": False
    }

    # Send question and get result
    response = requests.post(url, json=data)
    result = response.json()
    return result["response"]


# run MCP server
if __name__ == "__main__":
    mcp.run(transport="streamable-http")






