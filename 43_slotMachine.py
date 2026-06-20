# Python Slot Machine Game

import random


# Generate a row of 3 random slot symbols
def spin_row():
    symbols = ['⭐', '🍾', '🗽', '⛽']
    return [random.choice(symbols) for _ in range(3)]


# Display the generated row in a slot-machine format
def print_row(row):
    print("**************")
    print(" | ".join(row))
    print("**************")


# Calculate winnings based on matching symbols
def get_payout(row, bet):

    # Check if all three symbols match
    if row[0] == row[1] == row[2]:

        # Return payout multiplier based on symbol
        if row[0] == '⭐':
            return bet * 5
        elif row[0] == '🍾':
            return bet * 10
        elif row[0] == '🗽':
            return bet * 15
        elif row[0] == '⛽':
            return bet * 20

    # No match means no payout
    return 0


# Main game loop
def main():

    # Starting balance
    balance = 100

    print("Welcome to Python Slot Machine!")
    print("Symbols: ⭐ 🍾 🗽 ⛽")

    # Continue playing while the player has money
    while balance > 0:

        print(f"\nCurrent balance: ${balance}")

        # Get player's bet
        bet = input("Place your bet amount: ")

        # Validate that the input is a positive integer
        if not bet.isdigit():
            print("Please enter a valid number.")
            continue

        bet = int(bet)

        # Check if player has enough funds
        if bet > balance:
            print("Insufficient funds.")
            continue

        # Prevent zero or negative bets
        if bet <= 0:
            print("Bet must be greater than 0.")
            continue

        # Deduct bet from balance before spinning
        balance -= bet

        # Generate and display slot results
        row = spin_row()

        print("\nSpinning...\n")
        print_row(row)

        # Calculate winnings
        payout = get_payout(row, bet)

        # Display result of the spin
        if payout > 0:
            print(f"You won ${payout}!")
        else:
            print("Sorry, you lost this round.")

        # Add winnings back to balance
        balance += payout

        # Ask player if they want to continue
        play_again = input("Do you want to spin again? (Y/N): ").upper()

        if play_again != 'Y':
            break

    # Display final balance when game ends
    print(f"\nGame Over! Your final balance is ${balance}")



if __name__ == '__main__':
    main()