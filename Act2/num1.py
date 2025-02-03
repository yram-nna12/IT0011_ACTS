termF = int(input("Enter first term number: "))
termL = int(input("Enter first term number: "))

summation = 0
for num in range(termF, termL + 1):
    summation += num
    
print("\nThe sum of the numbers from", termF, "to", termL, "is", summation)