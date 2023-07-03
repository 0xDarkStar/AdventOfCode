import re

f = open("testInput.txt")
fileLines = []
for x in f:
    fileLines.append(x)

for x in fileLines:
    if " 1   2" in x:
        index = fileLines.index(x)
        break

cargo = {}
columns = int(fileLines[index][-3])
fileLines.reverse()

for x in range(columns):
    cargo[f"column{x+1}"] = []
    listIndex = fileLines[-index-1].index(str(x+1))
    for i in range(-index,0):
        if fileLines[i][listIndex] == " ":
            continue
        else:
            cargo[f"column{x+1}"].append(fileLines[i][listIndex])

fileLines.reverse()

instructions = r"move (\d+) from (\d+) to (\d+)"

for x in fileLines[index+2:]:
    matches = re.findall(instructions, x)
    x, y, z = matches[0]
    moveList = []
    for a in range(int(x)):
        moving = cargo[f"column{y}"].pop(-1)
        moveList.append(moving)
    moveList.reverse()
    for a in moveList:
        cargo[f"column{z}"].append(a)

for x in cargo:
    print(cargo[x][-1])