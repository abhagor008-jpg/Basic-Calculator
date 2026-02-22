a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = input("Enter the action to perform (+, -, /, *): ")

if c== "+":
    print(a + b)
elif c== "-":
    print(a - b)
elif c== "/":
    print(a / b)
elif c== "*":
    print(a * b)
else:
    print("Error")
