#Input - a function that prompts the users to enter data
#        Returns the entered data as a string

input()
input("What is your name?:")
name = input("What is your name?:")
print(f"hello {name}")
print("HAPPY BDAY!!")


age = input("What is your age?:")  #age is string
age = int(age)  #TypeCast is used. age is now int
age = age + 1
# age = int(input("What is your age?:")) ,  #TypeCast can also be used  as this 
print(f"You are {age} years old")

