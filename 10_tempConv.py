unit = input("Is this this temperature in Celsius or Fahrenhite (C/F):  ")
temp = float(input("Enter thr tempertature:"))
if unit == "C":
    temp = (round(9 * temp)/5 + 32, 1)
    print(f"the temperature in fahrenhite is: {temp} °F")
elif unit == "F":
    temp = (round(temp-32)*5/9, 1)
    print(f"the temperature in celsius is: {temp} °C")
else:
    print(f"{unit} is invaid unit of measurment")       