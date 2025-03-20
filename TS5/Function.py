def get_valid_integer(prompt):
    """Function to get a valid integer input from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("**Error: Please enter a valid integer.**")

def get_valid_choice():
    """Function to get a valid operation choice from the user."""
    while True:
        print("\nMathematical Operations:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        
        choice = input("Enter your choice: ").strip().upper()
        if choice in ['D', 'E', 'R', 'F']:
            return choice
        print("**Error: Invalid choice. Please try again.**")

def get_valid_second_number(choice, a):
    """Function to get a valid second number based on the operation."""
    while True:
        b = get_valid_integer("Enter 2nd number: ")
        if choice in ['D', 'R'] and b == 0:
            print("**Error: Denominator must not be zero. Try again.**")
        elif choice == 'F' and a >= b:
            print("**Error: Second number must be greater than the first. Try again.**")
        else:
            return b

def perform_operation(choice, a, b):
    """Function to perform the chosen mathematical operation."""
    if choice == 'D':
        print("RESULT:", a / b)
    elif choice == 'E':
        print("RESULT:", a ** b)
    elif choice == 'R':
        print("RESULT:", a % b)
    elif choice == 'F':
        print("RESULT:", sum(range(a, b + 1)))

def main():
    """Main function to run the program."""
    while True:
        choice = get_valid_choice()
        if choice == 'Q':
            print("Exiting the program.")
            break
        
        a = get_valid_integer("Enter 1st number: ")
        b = get_valid_second_number(choice, a)
        perform_operation(choice, a, b)

if __name__ == "__main__":
    main()
