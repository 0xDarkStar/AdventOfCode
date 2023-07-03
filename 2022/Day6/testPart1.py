f = open("testInput.txt", "r")
inputs = []
for x in f:
    x = x.replace("\n", "")
    inputs.append(x)

def find_repeats(myList):
    found = []
    times = 0
    howLong = 0
    for a in myList:
        howLong += 1
        if times == 4:
            break
        elif a in found:
            indexOfA = found.index(a)
            for b in range(indexOfA+1):
                found[b] = 9
            while 9 in found:
                found.remove(9)
            found.append(a)
            times = len(found)
        else:
            found.append(a)
            times += 1
    print(howLong-1)
    print(found)

for x in inputs:
    inputList = []
    for y in x:
        inputList.append(y)
    find_repeats(inputList)