
# A function to save address of person 
def save_address ():
     name = input("Enter name:")
     contact = input("Your contact:")
     address= input("Your address:")
     phone_num = input("Your phone number:")

     with open("address.txt", "a") as file:
            file.write(name + ", " + contact + ", " + address + ", " + phone + "\n")

     print("Saved successfully!")

