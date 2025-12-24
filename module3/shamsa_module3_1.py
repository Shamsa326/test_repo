
#calling library 

from fastapi import FastAPI

#create fastAPI application (app is the main function that will handle all requests)

app=FastAPI()

#Create an endpoint (URL)

@app.get("/hello")

#define function and query 

def hello(name: str):

    return {"message": f"Hello {name}"}


#Now run the server in the terminal:
#>> in the terminal : uvicorn shamsa_module3_1:app --reload
# 
#Test your API in the browser:
# http://127.0.0.1:8000/hello?name=Shamsa


#End
