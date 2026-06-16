import math #to get the value of pi ,e, square,.. etc
a = float(input("Enter the First value: "))
b = float(input("Enter the Second value: "))

addition = a+b
subtraction = a - b
multiplication = a*b
division = a/b
remainder = a%b

print(f"addition is: {addition}")
print(f"subtraction is: {subtraction}")
print(f"multiplication is: {multiplication}")
print(f"division is: {division}")
print(f"remainder is: {remainder}")


result = round(a)
print(f"round of a is: {result}")

result2 = abs(b)        #absolute value    |-11| = 11 
print(f"absolute value of b is: {result2}")

result3 = pow(b , 3)    #power 
print(f"3 to the power of b is: {result3}")

result4 = max(a, b)     #to check which is maximum
print(f"the maximum btwn a & b is: {result4}")

result5 = min(a, b)       #to check which is minimum
print(f"the mininmum value btwn a & b is: {result5}")

print(f"the value of pi is: {math.pi}")
print(f"the value of e is: {math.e}")

result6 = math.sqrt(a)
print(f"the square root of a is:{result6}")

result7 = math.ceil(b) 
#Ceiling division refers to dividing two numbers and rounding the result up to the nearest integer
print(result7)

result8 = math.floor(b)
#Floor Function in mathematics is the function that returns the greatest integer less than or equal to a given real number.
print(result8)