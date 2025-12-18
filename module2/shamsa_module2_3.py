

#Define a unique number function

def unique_numbers():
    #Ask user enter numbers
    nums = input("Enter numbers:")
    #removes any duplicate numbers and return it as sorted list 
    numbers=list(set(nums))
    numbers.sort()
    return numbers

print(unique_numbers())




