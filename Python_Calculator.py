
# Python Calculator(Addition, Subtraction, Multiplication, Division)

oprator = input("Enter operator (+, -, *, /): ")
num1 = float(input("Enter the 1st number: ")) 
num2 = float(input("Enter the 2nd number: "))

if oprator == "+":
    result = num1 + num2
    print(round(result, 2))
elif oprator == "-":
    result = num1 - num2
    print(round(result, 2))
elif oprator == "*":
    result = num1 * num2
    print(round(result, 2))
elif oprator == "/":
    result = num1 / num2
    print(round(result, 2))
else:
    print(f"{oprator} is not a valid operator.")
