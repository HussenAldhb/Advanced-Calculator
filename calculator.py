import math  # لاستخدام الجذر التربيعي

print("Welcome to the Advanced Calculator!")
print("Operations: +, -, *, /, sqrt (for square root)")

operation = input("Enter operation (+, -, *, /, sqrt): ")

if operation == "sqrt":
    num = float(input("Enter a number: "))
    result = math.sqrt(num)
    print(f"The square root of {num} is {result}")
else:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:  # لتجنب القسمة على صفر
            result = num1 / num2
        else:
            result = "Error: Cannot divide by zero!"
    else:
        result = "Error: Invalid operation!"
    print(f"{num1} {operation} {num2} = {result}")