list = ["python", "java", "javascript", "PHP", "swift"]
# print(list)
# print(list[1])
for i in list:  # here i interate the list items,items are called i
    print(i + " is a good language")

# str = "vajeed"
# for i in str:
#  print(i)

dict = {"1": "python", "2": "java", "3": "php"}
for i, j in dict.items():
    print(i, j)

for i in range(
    1, 101, 3
):  # steps 3 function it excludes the one number jumes to another number
    print(i)

# print number 1 to 100 with using number in program :

str1 = "."
str2 = ".........."

one = len(str1)
ten = len(str2)
for n in range(one, (ten * ten) + one):
    print(n)
