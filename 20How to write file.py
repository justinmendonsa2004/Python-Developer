file = open("19file.txt", "r+")  # at add, wt write code, rt read code
r = file.read()
print(r)

w = file.write("hacker\n")

file.close()
