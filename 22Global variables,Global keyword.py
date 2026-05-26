num = 50


def script():
    global num  # global keyword
    num = 10
    print(num)


script()
print(num)
