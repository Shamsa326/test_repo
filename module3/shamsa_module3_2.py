

#Import the libraries 

from fastapi import FastAPI
from datetime import datetime

#create fastAPI application 

app=FastAPI()


#Create an endpoint (URL) & define function and query 

@app.post("/message")
def send_message(message: str):
        time_now = datetime.now()
        return {
                "message" : message,
                "time_stamp": time_now
        }

#Now run the server in the terminal:
#>> in the terminal : uvicorn shamsa_module3_2:app --reload

#Test API in command prompt:
#curl -X POST "http://127.0.0.1:8000/message?message=Hello%20Hana"


#End

