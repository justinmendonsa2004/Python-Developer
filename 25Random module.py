import random

# # num = random.random()
# # num = random.randint(0, 100)
# list = [1, 2, 3, 4, 5]
# num = random.choice(list)
# print(num)

gnum = random.randint(0, 50)
attempts = 5

while attempts > 0:
    print("Attempts left", attempts)
    unum = int(input("Guess the number...."))
    if unum == gnum:
        print("you have won the game in ", attempts, "attempts")
        break
    elif unum > gnum:
        print("your number is too big")
    elif unum < gnum:
        print("your number is too small")
        # attempts = attempts -1
        attempts -= 1
    else:
        print("you have lost the game")  #
