#shopping cart

foods = []
prices = []
total = 0

while True:
    food =input("Enter your food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}:"))
        foods.append(food)
        prices.append(price)

print("-----YOUR CART-----")


for food in foods:
    print(food, end="")

for price in prices:
    total += price
    print(price)

print(f"your total bill is: {total}")
