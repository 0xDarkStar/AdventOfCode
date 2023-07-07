f = open("testInput.txt", "r")

systemFiles = {
}
currentLocation = ""
for x in f:
    print(currentLocation)
    x = x.replace("\n", "")
    if x[0] == "$":
        if x[2:4] == "cd":
            if x[5:] == "..":
                match len(currentLocation):
                    case 2:
                        currentLocation = currentLocation[:-1]
                    case value:
                        currentLocation = currentLocation[:-2]
            else:
                if x[5] == "/":
                    currentLocation += "/"
                    systemFiles[currentLocation] = []
                else:
                    if currentLocation[-1] == "/":
                        currentLocation += x[5:]
                        systemFiles[currentLocation] = []
                    else:
                        currentLocation += f"/{x[5:]}"
                        systemFiles[currentLocation] = []
    else:
        try:
            file = x.split(" ")
            x = f"{file[1]} {file[0]}"
            systemFiles[currentLocation].append(x)
        except KeyError:
            print(systemFiles)

for x in systemFiles:
    total = 0
    for y in systemFiles[x]:
        item = y.split(" ")
        print(item)
        if item[1] == "dir":
            continue
        else:
            total += int(item[1])
    if total <= 100000:
        print(x)
