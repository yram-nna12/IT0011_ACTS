number1 = float(input("Enter 1st number: "))
number2 = float(input("Enter 2nd number: "))
number3 = float(input("Enter 3rd number: "))

if number1 >= number2 and number1 >= number3:
    first = number1
    if number2 >= number3:
        second = number2
        third = number3
    else:
        second = number3
        third = number2
elif number2 >= number1 and number2 >= number3: 
    first = number2
    if number1 >= number3:
        second = number1
        third = number3
    else:
        second = number3
        third = number1
else: 
    first = number3
    if number1 >= number2:
        second = number1
        third = number2
    else:
        second = number2
        third = number1

print("Numbers in Descending Order: ", first, second, third)

    
    

