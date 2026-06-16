#weight conversion program
weight = float(input("Enter your weight: "))
unit = input("kilogram or pounds? (K/L): ")
if unit == "K":
    weight = weight*2.205
    unit = "LBS."
elif unit == "L":
    weight = weight/2.205
    unit = "Kgs."
else:
    print(f"{unit} was not valid")

print(f"your weight is {round(weight,3)}{unit}")