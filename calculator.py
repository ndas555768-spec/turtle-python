print("Simple Calculator")
print("Operations: +  -  *  /")

num1 = float(input("Enter first number: "))
op = input("Enter operator (+ - * /): ")
num2 = float(input("Enter second number: "))

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")
while True:
    print("\nCalculator")
    print("+  -  *  /")
    
    a = float(input("Enter first number: "))
    op = input("Operator: ")
    b = float(input("Enter second number: "))

    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        print("Result:", a / b if b != 0 else "Cannot divide by zero")
    else:
        print("Invalid operator")

    choice = input("Continue? (y/n): ")
    if choice.lower() != "y":
        break
