def digits(string):
    total = 0  

    for char in string:  
        if char.isdigit(): 
            total += int(char)  

    print("Sum of digits:", total) 

text = input("Enter a string with digits: ")
digits(text)
