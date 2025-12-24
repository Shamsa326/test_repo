
#Import libraries 

from fastapi import FastAPI
import sqlite3


#create fastAPI application 
app=FastAPI()


DB_NAME = "tasks.db"

#onnect to the Sql3 db and return that connection.

def get_db_connection():
    return sqlite3.connect(DB_NAME)

#Create an endpoint (URL) & define function and query 
@app.post("/add_tasks")
def add_tasks():
    conn = get_db_connection()
    cursor = conn.cursor()

 #Insert 2 rows
    cursor.execute("""
        INSERT INTO tasks (title, description, status)
        VALUES (?, ?, ?)
    """, ("Task 1", "First task description", "pending"))

    cursor.execute("""
        INSERT INTO tasks (title, description, status)
        VALUES (?, ?, ?)
    """, ("Task 2", "Second task description", "done"))

 #Save changes and close connection
    conn.commit()
    conn.close()

    return {"message": "2 tasks added successfully"}


#Now run the server in the terminal:
#>> in the terminal : uvicorn shamsa_module4_3:app --reload

#Test API in :
#http://127.0.0.1:8000/docs