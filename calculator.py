def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero"
    return a / b

print("Simple Calculator")
print("Choose an operation:")
print("+  -  *  /")

operation = input("Enter operation: ")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

except ValueError:
    print("Invalid number entered")
    exit()


if operation == "+":
    print("Result:", add(num1, num2))

elif operation == "-":
    print("Result:", subtract(num1, num2))

elif operation == "*":
    print("Result:", multiply(num1, num2))
