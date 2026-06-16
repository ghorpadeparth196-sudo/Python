# Membership Operator = used to test wheter a value or a variable is found in a sequence
#                       (string, list, tuples, set or dictionary)
#                       1.in
#                       2.not in

# word = "apple"
# letter = input("Guesss a letter in secret word: ")
# if letter in word:
#         print(f"There is a {letter}")
# else:
#         print(f"{letter} was not found in ")


# word = "apple"
# letter = input("Guesss a letter in secret word: ")
# if letter not in word:
#         print(f"{letter} was not found")
# else:
#          print(f"There is a {letter}")


# students = {"Parth", "Ajinkya", "Nishant"}
# student = input("Enter student name: ")
# if student in students:
#         print(f"{student} was found")
# else:
#        print(f"{student} was not found")

#DICTIONARY
# grades = {"Parth": "A", 
#           "Ajinkya": "B",
#           "Nishant": "C"}
# student = input("Enter student name: ") 
# if student in grades:
#         print(f"{student}'s grade is {grades[student]}")
# else:
#         print(f"{student} was not found")

#STRING
email = "parthghorpade21@gmail.com"
if "@" in email and "." in email:
        print("Valid")
else:
        print("Invalid")