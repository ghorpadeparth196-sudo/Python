# import time
# my_time = int(input("Enter the time in seconds: "))

# for x in range(my_time,0,-1):
#     print(x)
#     time.sleep(1)

# print("times up!")



import time
my_time = int(input("Enter the time in seconds: "))

for x in range(my_time,0,-1):
    print(x)
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = (x / 3600) % 24
    print(f"{seconds:02}:{minutes:02}:{hours:02}")
    time.sleep(1)

print("times up!")