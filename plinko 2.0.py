import random

# Slots and multipliers
SLOTS = [110, 41, 10, 5, 3, 1.5, 1, 0.5, 0.3, 0.5, 1, 1.5, 3, 5, 10, 41, 110]
ROWS = 16


# Drop the ball and return multiplier
def drop_ball():
    slot_position = 0
    for row in range(16):
        # If random returns 1, go right
        if random.randint(0, 1) == 1:
            slot_position += 1

    #see which slot it gets
    return SLOTS[slot_position]


# Print the board
def board():
    print("\n----------- Here's your board -----------")

    rows=18
    for i in range(2, rows):
        print("  " * (rows - i), end=" ")
        for i in range(i + 1):
            print(" . ", end=" ")
        print()

    print("    110  41  10   5   3  1.5  1  0.5 0.3 0.5  1  1.5  3   5  10   41  110")


# Get a valid bet
def get_bet(money):
    while True:
        try:
            bet=float(input("How much do you want to bet? "))
            if bet<=0:
                print("Bet must be greater than 0.")
            elif bet>money:
                print("You don't have enough money.")
            else:
                return bet
        except ValueError:
            print("Please enter a valid number.")


# Main game loop
def main():
    money=float(input("How much money to start with? "))

    while True:
        board()
        print(f"Current money: ${money:.2f}")

        bet=get_bet(money)
        money-=bet

        choice=input("Enter 1 to drop, 0 to quit: ")

        if choice=="0":
            break
        elif choice== "1":
            multiplier=drop_ball()
            winnings=bet * multiplier
            money+=winnings

            print(f"""
------------------------------------
You hit slot {multiplier}x
You won ${winnings:.2f}
You now have ${money:.2f}
------------------------------------
""")
        else:
            print("Please enter 1 or 0.")

        if money<=0:
            print("You're out of money!")
            break

main()
