# user input should be single latter
# if user input is cap the print cap latter
# if user input is lower then print lower letter
# if user input is num then print num
# special letter  @

uinput = input("Enter a string and its length should '1'")
len = len(uinput)

if len == 1:
    if uinput.isalpha():
        if uinput.isupper():
            print("user input is upper case")
        elif uinput.islower():
            print("userinput is Lower case")
    elif uinput.isnumeric():
        print("user input is numeric")
    else:
        print("user input is special char")
elif len > 1:
    print("Length of string is high")
else:
    print("String is too Short")
