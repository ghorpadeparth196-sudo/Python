import random

lowest_num = 0
highest_num = 100
answer=random.randint(lowest_num,highest_num)
guesses = 0
is_running=True

print("Python Number Guessing Game!")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guesses: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1
    if guess < lowest_num and guess > highest_num:
        print("That number is out of range!!")
        print(f"select a number between {lowest_num} and {highest_num}")
    elif guess < answer:
        print("TOO LOW! try again")
    elif guess> answer:
        print("TOO HIGH! try again")
    else:
        print(f"CORRECT! The answer was {answer}")
        print(f"Number of guesses: {guesses}")
