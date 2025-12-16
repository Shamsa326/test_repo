

def shift_text(text, price_per_letter):
    shifted = ""
    price = 0

    for ch in text:
        if ch.isalpha():
            shifted += chr(ord(ch) + 1)
            price += price_per_letter
        else:
            shifted += ch

    return {
        "shifted_string": shifted,
        "word_count": len(text.split()),
        "price": price
    }