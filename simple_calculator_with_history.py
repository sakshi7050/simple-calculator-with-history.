
# Simple Calculator with History

history = []

def calculate(a, b, operator):
    result = None
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        result = a / b if b != 0 else 'Error (divide by zero)'
    else:
        return 'Invalid operator'
    
    history.append(f"{a} {operator} {b} = {result}")
    return result

def show_history():
    print("\nCalculation History:")
    for h in history:
        print(h)

# Menu loop
while True:
    print("\n--- Simple Calculator ---")
    print("1. Calculate")
    print("2. Show History")
    print("3. Exit")
    
    choice = input("Enter choice (1/2/3): ")
    
    if choice == '1':
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            op = input("Enter operator (+, -, *, /): ")
            result = calculate(a, b, op)
            print("Result:", result)
        except ValueError:
            print("Invalid input. Please enter numbers.")
    elif choice == '2':
        show_history()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
