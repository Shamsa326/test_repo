

# A function to save address of person 

#making class and save the deatils on it
class person_address:
       def __init__(self,name:str,contact:str,address:str,phone_num:int):
              self.name = name 
              self.contact = contact
              self.address = address
              self.phone_num = phone_num 
       def save(self):
              file=open("person_address.txt", "w")
              file.write(self.name+","+self.contact+","+self.address+","+self.phone_num+".")
              file.close()

# input all details by user 
def input_det():
     name = input("Enter name:")
     contact = input("Your email:")
     address= input("Your address:")
     phone_num = input("Your phone number:")
     return person_address(name,contact,address,phone_num)

# calling  function and save it to go back class
person_address_=input_det()
person_address_.save()

