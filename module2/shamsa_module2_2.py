

# encrypt function for a string:

def encrypt():
    #Ask user to enter a text ONLY string type:

    text = str(input("Enter your text:"))
    shif_letter =""
    encrypt=[]
    #start to shift letter to encrypt the text 
    for ch in text:
         ch.isalpha()
         shif_letter = shif_letter + chr(ord(ch)+1 )
         encrypt= shif_letter
    return encrypt

#printing shifted text 
print(encrypt())

