import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"

def square(x):
    return x ** 2

def square_root(x):
    return math.sqrt(x)

while True:
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. Square Root")
    print("7. Exit")

    choice = input("Choose an option (1-7): ")

    if choice == '1':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", add(a, b))

    elif choice == '2':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", subtract(a, b))

    elif choice == '3':
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", multiply(a, b))

    elif choice == '4':
        a = float(input("Enter numerator: "))
        b = float(input("Enter denominator: "))
        print("Result:", divide(a, b))

    elif choice == '5':
        a = float(input("Enter a number: "))
        print("Square:", square(a))

    elif choice == '6':
        a = float(input("Enter a number: "))
        print("Square root:", square_root(a))

    elif choice == '7':
        print("Exiting calculator. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")