
#Import the libraries 
from fastapi import FastAPI
from pydantic import BaseModel
import random

#create fastAPI application 
app = FastAPI()

# In memory storage
person_data= {}

#create a data model
class Person(BaseModel):
    name:str
    phone_number:str

# POST API to add a person

@app.post("/person")
def create_person(person:Person):
    person_data["name"]=person.name
    person_data["phone_number"]=person.phone_number
    return {
        "message":"person data saved",
        "person":person_data
    }

# GET API to read person and add random number
@app.get("/person/random")
def read_person_with_random():
    if not person_data:
        return {"error":"No person data found"}
    
    random_number=random.randint(1,100)

    return {
        "name": person_data["name"],
        "phone_number": person_data["phone_number"],
        "random_number": random_number

       }
    
    
#Now run the server in the terminal:
#>> in the terminal : uvicorn shamsa_module3_4:app --reload
#
#
#End