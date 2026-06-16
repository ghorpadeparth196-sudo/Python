# keyword argument  = an argument proceded by an identifier
#                     helps with redability
#                     orders of arguments doesn't matter
#                     1. positional, 2. default, 3. keyword, 4. arbitrary


def hello(greetings,title,first,last):
    print(f"{greetings} {title}{first} {last}")
hello("Hello", "Mst.", "Parth", "Ghorpade")

# KEYWORD ARGUMENTS USED:
def hello(greetings,title,first,last):
    print(f"{greetings} {title}{first} {last}")
hello("Hello", title="Mst.", last="Ghorpade", first="Parth")