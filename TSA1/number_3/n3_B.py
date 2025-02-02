i = 1

numbers = [1, 3, 5, 6, 7]


while i <= len(numbers):
    j = 1
    while j <= (2*i - 1):
        print(numbers[i-1], end="")
        j += 1  
    print()  
    i += 1  
