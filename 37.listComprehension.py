#list comprehension = A concise way to create list in Python
#                     Compact and easier to read than traditional loops
#                     [expression for value in iterable if condition]

#NUMBERS
# doubles = [x*2 for x in range(1,11)]
# triple = [x*3 for x in range(1,11)]
# print(triple)

#STRINGS
# fruits = ["apple","banana", "mango", "watermelon"]
# # fruit = [fruit.upper() for fruit in fruits]
# fruit = [fruit[0] for fruit in fruits]
# print(fruit)

# #if CONDITION   
# numbers = [1,-2,3,-4,5,-6,7,-8]
# positve_num = [num for num in numbers if num>= 0]
# negative_num = [num for num in numbers if num<0]
# print(negative_num)

grades = [75,54,33,64,23,55]
passing_grades = [grade for grade in grades if grade > 35]
failing_grades = [grade for grade in grades if grade <= 35]
print(failing_grades)