"""Plinko Simulator."""
import random
import time
# Slots and multipliers
SLOTS = [110, 41, 10, 5, 3, 1.5, 1, 0.5, 0.3, 0.5, 1, 1.5, 3, 5, 10, 41, 110]
ROWS = 16


def create_player_profile():
    """Get player info and erturn as a dictionry."""
    
    name = input("Enter your name: ")
    location = input("Enter your location: ")

    profile = {'name': name,
               'location': location,
               'high_score': 0,
               'lifetime_losses': 0,
               'target_ads': False}
    return profile


def check_marketing_status(player_profile):
    """Check if player lost more than $500, if so sent out VIP OFFER."""
    
    if player_profile['lifetime_losses'] > 500 and player_profile['target_ads'] == False:
        print("VIP OFFER: Double your next deposit! Buy more credits now!")
        player_profile["target_ads"] = True

    elif player_profile['target_ads'] == False:
        print("Keep playing to climb the leaderboard!")


def drop_ball():
    """Simulate dropping a ball through the board."""
    
    slot_position = 0  # Start at far left

    # Loop through each row as the ball falls
    for row in range(ROWS):
        actual_row = row + 2  # Start counting from 2 to match board display
        # If random returns 1, go right
        if random.randint(0, 1) == 1:
            slot_position += 1

        # Prevent index out of bounds
        if slot_position < 0:
            slot_position = 0
        if slot_position > 16:
            slot_position = 16

        # Print the board with current ball position
        board(actual_row, slot_position)
        time.sleep(0.15)

    return SLOTS[slot_position]


def board(ball_row, ball_pos):
    """Print the ball and ball position."""
    
    print("\n----------- Here's your board -----------\n")

    rows = 18  # Total rows for display

    # Starting from row 2 to create triangular shape(skip row 0,1)
    for i in range(2, rows):
        # Print leading spaces to center the triangle
        print("  " * (rows - i), end=" ")

        # Print pegs(dots) and the ball
        for j in range(i + 1):

            if i == ball_row and j == ball_pos:
                print(" ● ", end=" ")  # Ball position
            else:
                print(" . ", end=" ")  # Peg

        print()

    print("\n    110  41  10   5   3  1.5  1  0.5 0.3 0.5  1  1.5  3   5  10   41  110")


def force_value(message, max_value = None):
    
    """Get a valid value, smaller than max value if there is one."""
    while True:
        try:
            value = float(input(message))

            # Check if valid
            if value <= 0:
                print("Enter a number greater than 0.")
            elif max_value is not None and value > max_value:
                print("You don't have enough money.")
            else:
                return value

        except ValueError:
            print("Please enter a valid number.")


def main():
    """Main game loop."""
    
    player_profile = create_player_profile()  # Create profile
    # Ask player for starting money
    money = force_value("How much money to start with: ?")

    while True:
        board(0, 0)  # Show initial board
        print(f"Current money: ${money:.2f}")

        # Ask user to continue or quite
        choice = input("Enter 1 to continue, 0 to quit: ")

        if choice == "0":
            print(player_profile['name'])
            print(player_profile['location'])
            print(f"""You have ${money:.2f} left
High score: ${player_profile['high_score']:.2f}
Total Losses: ${player_profile['lifetime_losses']:.2f}""")

            break  # Exit game

        elif choice == "1":
            bet = force_value("How much do you want to bet: ?", money)  # get user bet
            money -= bet  # Subtract bet from balance

            multiplier = drop_ball()  # Simulate ball drop
            winnings = bet * multiplier
            profit = winnings-bet
            money += winnings  # Add winnings to balance

            # Update player_profile
            if profit < 0:
                player_profile["lifetime_losses"] += abs(profit)
            if money > player_profile['high_score']:
                player_profile["high_score"] = money  

# Display result
            
            print(f"""
{"------------------------------------" if player_profile["target_ads"] == False else "-----♛------♕VIP♕------♛-----"}
You hit slot {multiplier}x
You won ${winnings:.2f}
You now have ${money:.2f}
High score: ${player_profile['high_score']:.2f}
Total Losses: ${player_profile['lifetime_losses']:.2f}
{"------------------------------------" if player_profile["target_ads"] == False else "-----♛------♕VIP♕------♛-----"}
""")

        else:
            print("Please enter 1 or 0.")
        # Check if player is out of money
        if money <= 0:
            print("You're out of money!")
            break

        check_marketing_status(player_profile)


if __name__ == "__main__":
    main()
