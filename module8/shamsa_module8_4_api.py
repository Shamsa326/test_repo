
from fastapi import FastAPI
import requests
import sqlite3

app = FastAPI()

# MCP_URL = "http://mcp:9000"   # MCP docker service name

@app.get("/status")
def status():
    return {"status": "ok"}

def save_user_info(name, phone):
    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT
                )
                """)

    conn.commit()
    cursor.execute("INSERT INTO users (name,phone) VALUES (?,?)",(name,phone))
    conn.commit()

def list_user_info():
    conn=sqlite3.connect("users.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows= cursor.fetchall()
    # for row in rows:
    #     print(row)
    return rows

@app.get("/adduser")
def adduser(name, phone):
    save_user_info(name, phone)
    return {"status": "ok"}

@app.get("/listusers")
def listusers():
    return list_user_info()