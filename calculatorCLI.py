print("🔢 Welcome to the Python CLI Calculator!")

print("Enter first number:")
num1 = float(input())

print("Enter second number:")
num2 = float(input())

print("Choose an operation: (+, -, *, /)")
operation = input()

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero!"
else:
    result = "Invalid operation."

print(f"🧮 Result: {result}")
