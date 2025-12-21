
#function of accpeting only string 


def accept_string (value):
        
    try:
        value.isalpha()
        print(value)
        return value
    except Exception:
        print("NULL")
        return None

#test both scenarios
accept_string("Shamsa")
accept_string(971)
