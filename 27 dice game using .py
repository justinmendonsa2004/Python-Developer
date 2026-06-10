import random

def roll():
    lis = [1, 2, 3, 4, 5, 6]
    num =random.choice(lis)
    print(num)
    
while True:   
    
    print("Do you want to play the Game")
    choice = input("Yes/No")
    if choice in "yes":
       print("How many players")
       nop = int(input("In numbers"))
       while True:
           for players in range(1, nop+1):
               print("Do you want to roll the dice")
               pc = int(input("Enter 1 to roll 0 to exit"))#jhhh
               if pc == 1:
                   roll()
               elif pc == 0:
                   break
               else:
                   print("invalid chioce") 
    elif choice in "no":
        break
    else:
        print("invalid choice")