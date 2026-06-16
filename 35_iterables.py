# iterables - An objects/collection that can return its element one at a time, 
#             allowing it to be iterated over in a loop


# numbers = [1,2,3,4,5]
# for num in numbers:
#     print(num)

# numbers = (1,2,3,4,5)
# for num in reversed(numbers):
#     print(num)

# fruits = {"Apple", "Mango", "Watermelon", "Banana"}
# for fruit in sorted(fruits):
#     print(fruit ,end=" , ")

my_dictionary = {"A":1, "B":2, "C":3}
for key, value in reversed(my_dictionary.items()):
    print(f"{key}: {value}")

