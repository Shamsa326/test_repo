

#Import the libraries 

from fastapi import FastAPI
from pydantic import BaseModel #to check (validate) the input data

#create fastAPI application 

app=FastAPI()

#create a data model

class Message(BaseModel):
    text: str

#Create an endpoint (URL) & define function and query 
@app.post("/message")

def create_message(data: Message):
    return {
        "message": data.text
    }

#Now run the server in the terminal:
#>> in the terminal : uvicorn shamsa_module3_3:app --reload

#Test API in :
#http://127.0.0.1:8000/docs


#End


