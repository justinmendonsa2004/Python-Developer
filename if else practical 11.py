age = int(input("Enter your age: "))

if age > 18:
    print("you are eligible for voting")
elif age == 18:
    conf = input("Do you have voter Id: ")

    if conf == "yes":
        print("you can vote")
    elif conf == "no":
        print("Apply for Voter Id")
    else:
        print("invalid input")
else:
    print("Manage Hogi POGo nodu")
