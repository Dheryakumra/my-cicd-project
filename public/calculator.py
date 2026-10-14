
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    print("=== Python Calculator ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choice = input("Choose an operation (1-4): ")
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        operations = {
            "1": add,
            "2": subtract,
            "3": multiply,
            "4": divide,
        }

        if choice not in operations:
            print("Invalid operation")
            return

        result = operations[choice](a, b)
        print("Result:", result)

    except ValueError as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
