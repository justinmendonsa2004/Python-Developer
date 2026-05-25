gnum = 55
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
        print("you have lost the game")
