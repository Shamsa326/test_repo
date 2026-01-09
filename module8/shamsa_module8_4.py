
#My application:


# import all libraries
import requests
from fastmcp import FastMCP
import sqlite3




db= "users.db"

#create MCP app 
mcp = FastMCP("My application")

# connect to db
def connect_db():
    return sqlite3.connect("users.db")

#create fastAPI application 
app=FastAPI()




# ----------------- LLM ---------------------







#--------------Create MCP tools----------------

@mcp.tool()
def show_data():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    db.close()
    return rows








#-------------- Start MCP server---------------

if __name__ == "__main__":
    mcp.run(transport="streamable-http")