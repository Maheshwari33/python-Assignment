#create a calculator using arithimetic operator

print("display all the operation")
print("addition")
print("subtraction")
print("multiplication")
print("division")

op = int(input("Select your operation: "))

if op == 1:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result of adding two numbers is:", num1 + num2)

elif op == 2:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result of subtracting two numbers is:", num1 - num2)

elif op == 3:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result of multiplying two numbers is:", num1 * num2)

elif op == 4:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num2 == 0:
        print("Cannot divide by zero!")        
    if num2 != 0:
        print("Result of dividing two numbers is:", num1 / num2)
    else:
        print("Cannot divide by zero!")
else:op = int(input("Select your operation: "))
if op == 1:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result of adding two numbers is:", num1 + num2)
elif op == 2:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result of subtracting two numbers is:", num1 - num2)
elif op == 3:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result of multiplying two numbers is:", num1 * num2)
elif op == 4:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num2 == 0:
        print("Cannot divide by zero!")        
    if num2 != 0:
        print("Result of dividing two numbers is:", num1 / num2)
    else:
        print("Cannot divide by zero!")

else:
    print("Invalid operation")
    print("Invalid operation")
