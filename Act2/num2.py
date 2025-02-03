inputNum = int(input("Enter a number: "))

if inputNum > 1:
    is_a_prime = True
    for i in range(2, inputNum):
        if inputNum % i == 0:
            is_a_prime = False
            break
    if is_a_prime:
        print(inputNum, "is a prime number.")
    else:
        print(inputNum, "is not a prime number.")
else:
    print(inputNum, "is not a prime number.")