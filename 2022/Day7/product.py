f = open("input.txt", "r")

systemFiles = {} # Hold all directories
currentLocation = "" # Store the path to current location
for command in f: # Looks through all the commands and outputs
    command = command.replace("\n", "") # Cleans line
    if command[0] == "$": # Is it a command?
        if "cd" in command:
            if command[5:] == "..": # Do they want to go back?
                curPath = currentLocation.split("/") # Turn the path into a list
                if len(curPath) == 2:
                    currentLocation = "/"
                else:
                    currentLocation = "/".join(curPath[:-1]) # Remove the final dir from the list
            else: # They want to go somewhere
                if command[5] == "/": # They are going into the root directory
                    currentLocation += "/" # They're now in root
                    systemFiles[currentLocation] = [] # Make the first dict for the dir
                else: # They're going into a dir
                    curPath = currentLocation.split("/") # How long is the path
                    if len(curPath[-1]) == 0: # They're in the root dir
                        currentLocation += f"{command[5:]}" # Don't add another /
                    else: # They're in another dir
                        currentLocation += f"/{command[5:]}"
                    systemFiles[currentLocation] = [] # Add this dir to the dict
    else: # It is a file or dir from a ls
        try:
            file = command.split(" ") # Grab the type/size and the file/dir name
            command = f"{file[1]} {file[0]}" # Order it into "Name Type/Size"
            systemFiles[currentLocation].append(command)
        except KeyError:
            print(systemFiles) # Find out where tf I went wrong

dirSizes = {} # Hold the sizes of all of them

for file in systemFiles: # Look at all the dirs
    dirSizes[file] = 0 # Add it to this dict

for file in systemFiles: # Look at all the dirs
    for y in systemFiles[file]: # Look inside the dirs
        item = y.split(" ")
        if item[1] == "dir": # This item is another dir
            continue
        else: # It isn't a dir
            dirSizes[file] += int(item[1]) # Add the size to the size of the dir

invertedList = list(dirSizes.keys())
invertedList.reverse()

for dir in invertedList: # Look at the inverted list to be seeing the sub dirs first
    for y in systemFiles[dir]: # Look inside this dir
        item = y.split(" ")
        if item[1] == "dir": # There's a dir!
            if dir == "/": # We're in root
                subDir = f"{dir}{item[0]}" # Make the path of the dir we're looking at
            else: # We're not in root
                subDir = f"{dir}/{item[0]}" # Make the path of the dir we're looking at
            dirSizes[dir] += dirSizes[subDir] # Add the size of that dir to the current dir we're in

total = 0
for file in dirSizes: # Look at all the dirs
    if dirSizes[file] <= 100000: # They're smaller than 100,000
        total += dirSizes[file]

print(total) # Size of all dirs smaller than 100,000
unusedSpace = 70000000 - dirSizes["/"] # Space left
bigEnough = []

for file in dirSizes:
    if unusedSpace+dirSizes[file] >= 30000000: # If removed, we'll have enough space for the update
        bigEnough.append(file)

smallestSize = 99999999999999999999999999999999999 
for file in bigEnough: # You know how this goes by now
    if dirSizes[file] < smallestSize:
        smallestSize = dirSizes[file]
        smallestDir = file
print(f"{smallestDir} Size: {smallestSize}") # Smallest directory that, if removed, will free up enough space for the update
