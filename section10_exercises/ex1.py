linenumber = 1

with open("file.txt") as file:
    for line in file:
        print("{} {}".format(linenumber, line.rstrip()))
        linenumber += 1