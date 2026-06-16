#dictionary = a collection of {key:value} pairs
#             ordered and changeable. No duplicates

capitals = {"India":"New Delhi",
            "Germany": "Berlin",
            "USA":"D.C Washington"}

# print(capitals)
print("keys: ")
key = capitals.keys
for key in capitals:
    print(key)
print()
print("values: ")
values = capitals.values
for values in capitals:
    print(values)

items = capitals.items
for key, values in capitals.items():
    print(f"{key}:{values}")