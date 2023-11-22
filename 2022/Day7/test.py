currentLoc = "/home/test"
dirs = currentLoc.split("/")
print(dirs)
currentLoc = "/".join(dirs[:-1])
print(currentLoc)