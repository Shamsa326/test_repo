
#function of accpeting only string 


def accept_string (value):
        
    try:
        value.upper()
        print(value)
        return value
    except Exception:
        print("NULL")
        return None

#test both scenarios
accept_string("SHAMSA")
accept_string(111)
