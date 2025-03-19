while True:
    print("\nMathematical Operations:")
    print("[D] - Divide")
    print("[E] - Exponentiation")
    print("[R] - Remainder")
    print("[F] - Summation")
    # Get user choice and convert to uppercase
    choice = input("Enter your choice: ").strip().upper()  
    # Loop to ensure valid first number
    while True:  
        try:
            a = int(input("Enter 1st number: ")) 
            break  
        except ValueError: # Handle invalid input
            print("**Error: Please enter a valid integer.**")  
    # Loop to ensure valid second number
    while True: 
        try:
            b = int(input("Enter 2nd number: ")) 

            # Validate based on the chosen operation
            if choice == 'D' or choice == 'R':  # Check for Division & Remainder
                if b == 0:
                    print("**Error: Denominator must not be zero. Try again.**")  # Prevent division by zero
                    continue  # Ask for input again
            elif choice == 'F':  # Check for Summation condition
                if a >= b:
                    print("**Error: Second number must be greater than the first. Try again.**")  # Ensure valid range
                    continue  # Ask for input again
            # Exit loop if input is valid
            break  
        # Handle invalid input
        except ValueError:
            print("**Error: Please enter a valid integer.**")  

    # Perform operations after valid inputs 
    # Division
    if choice == 'D': 
        print("RESULT:", a / b)
    # Exponentiation
    elif choice == 'E':
        print("RESULT:", a ** b)
    # Remainder
    elif choice == 'R':
        print("RESULT:", a % b)
    # Summation
    elif choice == 'F': 
        # Compute and display sum from a to b
        print("RESULT:", sum(range(a, b + 1)))  
    # Handle invalid menu choice
    else:
        print("Invalid choice. Please try again.")  