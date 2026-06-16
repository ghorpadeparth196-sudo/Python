# *args = allows you to pas multiple non-key arguments
# **kwargs = allows you to pass multiple kwywors arguments
#            * unpacking operator
#            1. positional, 2. default, 3. keyword, 4. arbitrary



#args:-
# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
# print(add(1,2,3,4))


# def display_name(*args):
#     for name in args:
#         print(name, end=" ")
# display_name("Mst.", "Parth", "Ghorpade")

#kwargs:-
# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")

# print_address(Building = "1/D, 501 kalpatru build",
#               Society = "Devratnanagar, chunabhatti",
#               city = "Mumbai",
#               code = "400022")

# args $ kwargs
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")

    print()

    for value in kwargs.values():
        print(value, end=" ")

shipping_label(
    "Mst.", "Parth", "Ghorpade",
    Building="1/D, 501 kalpatru build",
    Society="Devratnanagar, chunabhatti",
    city="Mumbai",
    code="400022"
)
