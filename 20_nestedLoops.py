# nested loops = a loops within another loops (outer , inner)
#                outer loops:
#                        inner loops:

rows = int(input("enter number of rows: "))
columns = int(input("enter number of columns: "))
symbol = input("enter your symbol: ")

for x in range (rows):
    for y in range(columns):
        print(symbol, end="")
    print()