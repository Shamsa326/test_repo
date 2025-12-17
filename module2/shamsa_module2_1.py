

# A function to show if number even or odd by enetring a number from the user.

def even_or_odd():
    try:
        number = int(input("Enter a number:"))
        if number %2 ==0:
            print("Even")
        else :
            print("Odd")
    except Exception:
         print("typeError")
even_or_odd()        

