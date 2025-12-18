
#calling library 

import json 

#making class 
class people:
    def __init__(self,name:str,number:int,location:str,job_title:str):
            self.name = name 
            self.number = number
            self.location = location
            self.job_title = job_title 

    #converts class objects into JSON format     
    def to_dict(self):
        return {
            "name": self.name,
            "number": self.number,
            "location": self.location,
            "job_title": self.job_title
        }

#input all details by user:

def input_det():
     name = input("Enter name:")
     number = input("Your number:")
     location= input("Your location:")
     job_title = input("Your job title:")
     return people (name,number,location,job_title)

#count for 5 people only:
ppl=[]    
for _ in range(5):
    p=input_det()
    ppl.append(p.to_dict())

# Save to JSON file
with open("people_info.json", "w") as file:
    json.dump(ppl, file,indent=4)


