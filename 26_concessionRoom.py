menu = {"pizza":250,
        "burger":300,
        "samosa":140,
        "nachos":170,
        "popcorns":200,
        "coke":66}

cart = []
total = 0

print("-----MENU-----")
for key, value in menu.items():
    print(f"{key:10}:{value}")
print("---------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print("Item not available!")

print("-------YOUR ORDER---------")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
print("\n--------------------------")

print(f"Total is: {total:.2f}")