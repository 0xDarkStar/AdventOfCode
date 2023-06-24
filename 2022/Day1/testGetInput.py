# Testing how to get the input from the webpage to the code.

# Method #1: Copy all the numbers and put it into a .txt file. Read the file and try to make a matrix.
from re import search

f = open("testInput.txt", "r")
fileLines = []
for x in f:
    fileLines.append(x)
print(fileLines)

f = open("testMatrix.txt", "w")
f.write("[[")
previous = "["
for x in fileLines:
    if x == "\n":
        f.write("]")
        previous = "]"
    elif previous == "[":
        x = x.replace("\n", "")
        f.write(x)
        previous = x
    elif search(".[0-9]", previous):
        x = x.replace("\n", "")
        f.write(f", {x}")
        previous = x
    else:
        x = x.replace("\n", "")
        f.write(f", [{x}")
        previous = x
f.write("]]")
f.close()
f = open("testMatrix.txt", "r")
content = f.read()
elfList = eval(content)
print(elfList)

# Method #1 works great.