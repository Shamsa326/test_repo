
from fastapi import FastAPI
from datetime import datetime


app= FastAPI()

@app.post("/health")
def health_server():
    return {
        "status": "healthy",
        "server_time": datetime.now()
    }

@app.get("/")
def root():
    return {"message": "FastAPI server is running"}


#uvicorn shamsa_module7_3:app --reload
