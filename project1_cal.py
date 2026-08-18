# Simple Calculator
print("        SIMPLE CALCULATOR")
while True:

    print("\nChoose an operation:")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")
    print("%  Modulus")
    print("q  Quit")

    operation = input("\nEnter operation: ")

    if operation.lower() == "q":
        print("\nThank you for using the calculator!")
        break

    if operation not in ["+", "-", "*", "/", "%"]:
        print("Invalid operation! Please try again.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operation == "+":
            result = num1 + num2

        elif operation == "-":
            result = num1 - num2

        elif operation == "*":
            result = num1 * num2

        elif operation == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero!")
                continue
            result = num1 / num2

        elif operation == "%":
            if num2 == 0:
                print("Error: Cannot divide by zero!")
                continue
            result = num1 % num2

        print("\n------------------------------")
        print(f"Result: {num1} {operation} {num2} = {result}")
        print("------------------------------")

    except ValueError:
        print("Invalid input! Please enter numbers only.")