
import sqlite3
from fastmcp import FastMCP


#create MCP app 
mcp = FastMCP("SQL MCP")

# connect to db
def connect_db():
    return sqlite3.connect("data.db")

# create MCP tools

@mcp.tool()
def show_data():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM data")
    rows = cursor.fetchall()
    db.close()
    return rows


# Start MCP server
if __name__ == "__main__":
    mcp.run(transport="streamable-http")

