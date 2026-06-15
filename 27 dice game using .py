import random
pc = 2

def roll(player):
    lis = [1, 2, 3, 4, 5, 6]
    num =random.choice(lis)
    print(f"player {player} You have got {num} value")
    
while True:   
    
    print("Do you want to play the Game")
    choice = input("Yes/No")
    if choice in "yes":
       print("How many players")
       nop = int(input("In numbers"))
       while pc != 0:
           for player in range(1, nop+1):
               print("Do you want to roll the dice player {player}")
               pc = int(input("Enter 1 to roll 0 to exit"))
               if pc == 1:
                   roll(player)
               elif pc == 0:
                   break
               else:
                   print("invalid chioce") 
    elif choice in "no":
        break
    else:
        print("invalid choice")