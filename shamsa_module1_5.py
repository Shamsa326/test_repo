

#python function given a string of words and price for a letter

def text_price (text,price_letter):

    shif_letter =""
    price= 0
    #count shifted letter and price 
    for ch in text :
        if ch.isalpha():
            shif_letter = shif_letter + chr(ord(ch)+1 )
            price = price + price_letter
        else :
            shif_letter= shif_letter + ch 
    return { "shifted_string": shif_letter ,
           "word_count" : len(text.split()) ,
           "price_of_string": price
             }

print(text_price("Shamsa", 2))