# READ mood...
file = open("19file.txt")

r = file.read()
for ltr in r:
    print(ltr)

file.close()
