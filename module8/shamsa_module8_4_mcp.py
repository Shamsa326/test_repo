import users
#My application:


# import library
from fastmcp import FastMCP
import sqlite3


mcp = FastMCP("MCP Server")

#create mcp tool
@mcp.tool()
def save_user_info(name:str, phone:str):
   
    return users.save_user_info(name, phone)

@mcp.tool()
def display_user_info():
   
    return users.list_user_info()

if __name__ == "__main__":
    mcp.run(host="0.0.0.0", port=9000)

