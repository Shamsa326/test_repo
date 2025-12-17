

#count word for each address

def word_count (filename="person_address.txt"):
    lines = ""
    char_len = 0
    #reads the whole file and count the word on it
    with open(filename,"r") as file:
        lines = file.readline()
        word_len=lines.split(",")  
        char_len = len(word_len)

    #add the string to the end of the file
    with open(filename,"a") as file:
        file.write(str(char_len))
    
    
word_count()