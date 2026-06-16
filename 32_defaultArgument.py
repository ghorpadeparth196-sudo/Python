#default arguments = A default value for certain parameter
#                    a default is used when that  argument is omitted make your function more flexible,
#                    reduces # of arguments
#                    1. positional, 2. default, 3. keyword, 4. arbitrary


# def net_price(list_price, discount=0, tax=0.05):
#     return list_price*(1-discount)*(1+tax)
# print(net_price(500))

import time
def count(start, end):
    for x in range(start,end):
        print(x)
        time.sleep(1)
    print("Hooray!")
count(100,105)

