principle = 0
intrest  = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle<0:
        print("principle amount cannot be less than zero")
    else: 
        break

while True:
    rate = float(input("Enter the intrest amount: "))
    if intrest<0:
        print("intrest amount cannot be less than zero")
    else: 
        break   

while True:
    time = int(input("Enter the time amount: "))
    if time<0:
        print("time years cannot be less than zero")
    else: 
        break 
total = principle*pow((1 + rate /100),time)
print(f"Total amount is: {total}")