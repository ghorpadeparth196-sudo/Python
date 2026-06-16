#function - a block of reusable code
#           place() after  the functionname to invoke it

# def happy_birthday(name, age):
#     print(f"Happy bday to you {name}!")
#     print(f"You are {age} years old")
#     print("Happy bday to you!")
#     print()

# happy_birthday("Parth", 20)
# happy_birthday("Ajinkya", 23)

# def id_card(name, age, uid_no):
#     print(f"My name is {name} ")
#     print(f"I am {age} years old")
#     print(f"My UID number is {uid_no}")
#     print()

# id_card("Parth Ghorpade", 20, "124AM1289A")
# id_card("Ajinkya Ghorpade", 23, "124AB1289A")

#Return - statement used to ena a function and send a result back to the caller

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
full_name = create_name("Parth" , "Ghorpade")
print(full_name)


def calculator(x,y):
    return x+y
print(calculator(2,4))
