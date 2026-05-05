import random
import time
# Slots and multipliers
SLOTS = [110, 41, 10, 5, 3, 1.5, 1, 0.5, 0.3, 0.5, 1, 1.5, 3, 5, 10, 41, 110]
ROWS=16




# Simulate dropping a ball through the board
def drop_ball():
    slot_position = 0#Start at far left

    #Loop through each row as the ball falls
    for row in range(16): 
        actual_row= row+2 # Start counting from 2 to match board display
        #If random returns 1, go right
        if random.randint(0, 1)== 1:
            slot_position+= 1
            
        #Prevent index out of bounds
        if slot_position< 0:
            slot_position=0
        if slot_position >16:
            slot_position =16
        
        #Print the board with current ball position
        board(actual_row, slot_position)
        time.sleep(0.01)
    
    return SLOTS[slot_position]




# Print the board and ball position
def board(ball_row, ball_pos):
    print("\n----------- Here's your board -----------\n")

    rows=18 #Total rows for display
    
    #Starting from row 2 to create triangular shape(skip row 0,1)
    for i in range(2, rows):
        #Print leading spaces to center the triangle
        print("  " * (rows - i), end=" ")
        
        #Print pegs(dots) and the ball
        for j in range(i + 1):
            
            if i == ball_row and j == ball_pos:
                print(" ● ", end=" ")#Ball position
            else:
                print(" . ", end=" ")#Peg

        print()

    print("\n    110  41  10   5   3  1.5  1  0.5 0.3 0.5  1  1.5  3   5  10   41  110")



# Get a valid bet
def force_bet(money):
    while True:
        try:
            bet=float(input("How much do you want to bet? "))

            #Check if bet is valid
            if bet<=0:
                print("Bet must be greater than 0.")
            elif bet>money:
                print("You don't have enough money.")
            else:
                return bet#Valid bet
            
        except ValueError:
            print("Please enter a valid number.")




# Main game loop
def main():
    #Ask player for starting money
    money=float(input("How much money to start with? "))

    while True:
        board(2,1) #Show initial board(ball at top center)
        print(f"Current money: ${money:.2f}")

        bet=force_bet(money)#get user bet
        money-=bet#Subtract bet from balance
        
        #Ask user to continue or quite
        choice=input("Enter 1 to drop, 0 to quit: ")

        if choice=="0":
            break #Exit game
        
        elif choice== "1":
            multiplier=drop_ball()#Simulate ball drop
            winnings=bet * multiplier#CAlculate winnings
            money+=winnings#Add winnings to balance

            #Display result
            print(f"""
------------------------------------
You hit slot {multiplier}x
You won ${winnings:.2f}
You now have ${money:.2f}
------------------------------------
""")
        else:
            print("Please enter 1 or 0.")
        #Check if player is out of money
        if money<=0:
            print("You're out of money!")
            break

if __name__=="__main__":
    main()
