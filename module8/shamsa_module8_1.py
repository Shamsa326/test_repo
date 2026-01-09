

from fastmcp import FastMCP 
from datetime import datetime
import random


#create MCP app 
mcp = FastMCP("Shamsa's MCP Server")


#create mcp tools:

@mcp.tool()
def system_date():
    sys_date =datetime.now()
    return sys_date

@mcp.tool()
def random_number():
    random_num = random.randint(1,100)
    return random_num


#run MCP server
if __name__ == "__main__":
    mcp.run(transport="streamable-http")


#  in terminal :
# pip install fastmcp
# npx @modelcontextprotocol/inspector

# run in terminal :
# python shamsa_module8_1.py
# open cmd and type : npx @modelcontextprotocol/inspector


