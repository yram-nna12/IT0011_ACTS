def get_choice():
    print("\nMathematical Operations:")
    print("[D] - Divide")
    print("[E] - Exponentiation")
    print("[R] - Remainder")
    print("[F] - Summation")
    return input("Enter your choice: ").strip().upper()

def get_valid_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("**Error: Please enter a valid integer.**")

def get_valid_numbers(choice):
    a = get_valid_integer("Enter 1st number: ")
    while True:
        b = get_valid_integer("Enter 2nd number: ")
        if choice in ('D', 'R') and b == 0:
            print("**Error: Denominator must not be zero. Try again.**")
        elif choice == 'F' and a >= b:
            print("**Error: Second number must be greater than the first. Try again.**")
        else:
            return a, b

def perform_operation(choice, a, b):
    operations = {
        'D': lambda x, y: x / y,
        'E': lambda x, y: x ** y,
        'R': lambda x, y: x % y,
        'F': lambda x, y: sum(range(x, y + 1))
    }
    result = operations.get(choice, lambda x, y: "Invalid choice. Please try again.")(a, b)
    print("RESULT:", result)

def main():
    while True:
        choice = get_choice()
        a, b = get_valid_numbers(choice)
        perform_operation(choice, a, b)

if __name__ == "__main__":
    main()
