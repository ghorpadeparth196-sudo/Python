#calculator
operator = input("Enter  operator (+ - * /): ")
num1 = float(input("Enter num 1: "))
num2 = float(input("Enter num 2: "))

if operator == "+":
    result= num1+num2
    print(round(result))

elif operator == "-":
    result= num1-num2
    print(round(result))

elif operator == "*":
    result= num1*num2
    print(round(result))

elif operator == "/":
    result= num1/num2
    print(round(result))
else:
    print("invalid")