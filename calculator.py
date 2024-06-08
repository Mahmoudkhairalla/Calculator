# calculator.py

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error! Division by zero." if y == 0 else x / y

operations = {
    '1': ('Add', add),
    '2': ('Subtract', subtract),
    '3': ('Multiply', multiply),
    '4': ('Divide', divide)
}

def perform_operation(choice, num1, num2):
    name, func = operations[choice]
    return f"{num1} {name} {num2} = {func(num1, num2)}"

# module.py

from calculator import operations, perform_operation

def main():
    print("Simple Calculator")
    for key, (name, _) in operations.items():
        print(f"{key}. {name}")

    while True:
        choice = input("Enter choice (1/2/3/4): ")
        if choice in operations:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(perform_operation(choice, num1, num2))
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("Invalid Input. Please select a valid operation.")

        if input("Do you want to perform another calculation? (yes/no): ").lower() != 'yes':
            break

if __name__ == "__main__":
    main()