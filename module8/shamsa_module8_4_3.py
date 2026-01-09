import sqlite3
from fastmcp import FastMCP

def store_into_database():
    db = sqlite3.connect("users.db")
    cursor = db.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER,
        name TEXT,
        age INTEGER
    )
    """)
    cursor.execute("INSERT INTO data VALUES (1, 'Shamsa', '15')")
    cursor.execute("INSERT INTO data VALUES (2, 'Hana','16')")
    cursor.execute("INSERT INTO data VALUES (3, 'Theyab','3')")
    db.commit()
    db.close()

mcp = FastMCP()

@mcp.tool()
def ask_question(question:str):
    return {
        "question" : question
    }

if __name__ == "__main__" : 
    mcp.run(transport="streamable-http")