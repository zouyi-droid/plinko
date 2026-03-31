import random
#Menu

#Ask user how much thet want to bet
money=float(input("How much money to start with?"))
slots_list=[110, 41, 10, 5, 3, 1.5, 1, 0.5, 0.3, 0.5, 1, 1.5, 3, 5, 10, 41, 110]

#Function to find out what slot the ball lands on.
def drop(slots_list):
    slot_position = 0
    for row in range(16):
        # If random returns 1, go right
        if random.randint(0, 1) == 1:
            slot_position += 1

    #see which slot it gets
    return slots_list[slot_position]



#print the board and the slots
def board():
    print("                  -----------Here's your board-----------")
    rows=18
    for i in range(2,rows):
        print("  "*(rows-i), end=" " )
        for j in range(i+1):
            print(" . ", end=" ")
        print()
    print("    110  41  10   5   3  1.5  1  0.5 0.3 0.5  1  1.5  3   5  10   41  110")

def force(message):
    while True:
        try:
            bet=float(input(message))
            if bet <= 0 or bet > money:
                print("That amount is not valid")
           
            else:
                return bet
        except ValueError:
            print("Please enter a valid number")
             
   


while True:
    board()
    bet=force("How much you want to bet?")
    money-=bet
    x=input("Enter 1 to drop, enter 0 to stop")

    if x=="0":
        break
    elif x == "1":
        final_slot=drop(slots_list)
        amount=bet*final_slot

        money+=amount
        money=round(money,2)
        print("""
------------------------------------
You hit slot {}, You now have ${}
------------------------------------""".format(final_slot, money))
    else:
        print("Please enter 1 or 0")
        x=input("Enter 1 to drop, enter 0 to stop")
        


