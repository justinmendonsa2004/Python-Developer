"""import os
def player():
    directory = r"E:\MUSIC"
    list = os.listdir(directory)
    # print(files)
    for i in list:
        print(i)
     n = input("select your song using index number:")
     if n.isnumeric():
      n =int(n)
      os.startfile(os.path.join(directory,list[n]))

      else:
     print("invalid selection")

player()"""

import os


def player():
    directory = r"E:\MUSIC"
    songs = os.listdir(directory)

    # Print songs with index
    for i in range(len(songs)):
        print(i, ":", songs[i])

    n = input("Select your song using index number: ")

    if n.isnumeric():
        n = int(n)

        if 0 <= n < len(songs):
            os.startfile(os.path.join(directory, songs[n]))
        else:
            print("Index out of range")

    else:
        print("Invalid selection")


player()
