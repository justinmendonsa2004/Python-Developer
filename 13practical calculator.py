print("Press 1 for Addition")
print("Press 2 for Subtraction")
print("Press 3 for Multiplication")
print("Press 4 for Division")
print("=========================")

choice = int(input("Enter your choice \n"))
num1 = int(input("Enter your first number \n"))
num2 = int(input("Enter your Second number \n"))


if choice == 1:
    print("addition of two number is = ", num1 + num2)
elif choice == 2:
    print("Subtraction of two number is = ", num1 - num2)
elif choice == 3:
    print("Multiplication of two number is = ", num1 * num2)
elif choice == 4:
    print("Division of two number is = ", num1 / num2)
else:
    print("Invalid option")
