def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def main():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Enter an operation (+, -, *, /): ")

            if operation == "+":
                result = add(num1, num2)
            elif operation == "-":
                result = subtract(num1, num2)
            elif operation == "*":
                result = multiply(num1, num2)
            elif operation == "/":
                result = divide(num1, num2)
            else:
                print("Invalid operation. Please try again.")
                continue

            print(f"Result: {result}")

            continue_calculation = input("Do you want to continue? (yes/no): ")
            if continue_calculation.lower() != "yes":
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()