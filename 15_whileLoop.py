# While loop = execute some code WHILE some condition remain true


# age = int(input("Enter your age: "))
# while age<0:
#     print("age can not be negative")
#     age = int(input("Enter your age: "))
# print(f"you are {age} years old")

# food = input("Enter the food you like (q to quit):")
# while not food == "q":
#     print(f"you like {food}")
#     food = input("Enter the food you like (q to quit):")
# print("bye")

num = int(input("Enter a number btwn 1-10: "))
while num<1 or num>10:
    print(f"{num} is not valid")
    num = int(input("Enter a number btwn 1-10"))
print(f"your number is: {num}")
