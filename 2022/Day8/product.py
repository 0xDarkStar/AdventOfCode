f = open("input.txt", "r")

trees = []

for line in f:
    line = line.replace("\n", "")
    treeLine = list(line)
    trees.append(treeLine)

xInd = 1
yInd = 1

xLimit = len(treeLine)
yLimit = len(trees)


def isSeen(xInd, yInd):
    seenLeft = True
    seenRight = True
    seenTop = True
    seenBottom = True
    maxHeight = int(trees[yInd][xInd])-1
    for x in range(xInd):
        if int(trees[yInd][x]) > maxHeight:
            seenLeft = False
            break
    for x in range(xInd+1, xLimit):
        if int(trees[yInd][x]) > maxHeight:
            seenRight = False
            break
    for y in range(yInd):
        if int(trees[y][xInd]) > maxHeight:
            seenTop = False
    for y in range(yInd+1, yLimit):
        if int(trees[y][xInd]) > maxHeight:
            seenBottom = False
    if seenBottom == True or seenTop == True or seenRight == True or seenLeft == True:
        return 1
    else:
        return 0

treesSeen = 0

scenicScores = []
def scenicScore(xInd, yInd):
    curTree = int(trees[yInd][xInd])
    # Go up
    while True:
        y = yInd-1
        uScore = 0
        while y >= 0:
            uScore += 1
            if int(trees[y][xInd]) >= curTree:
                break
            y -= 1
        break
    # Go down
    while True:
        y = yInd+1
        dScore = 0
        while y <= yLimit-1:
            dScore += 1
            if int(trees[y][xInd]) >= curTree:
                break
            y += 1
        break
    # Go right
    while True:
        x = xInd+1
        rScore = 0
        while x <= xLimit-1:
            rScore += 1
            if int(trees[yInd][x]) >= curTree:
                break
            x += 1
        break
    # Go left
    while True:
        x = xInd-1
        lScore = 0
        while x >= 0:
            lScore += 1
            if int(trees[yInd][x]) >= curTree:
                break
            x -= 1
        break
    score = uScore*dScore*rScore*lScore
    scenicScores.append(score)

for treeLine in trees:
    if yInd == yLimit-1:
        break
    xInd = 1
    for tree in treeLine:
        if xInd == xLimit-1:
            break
        treesSeen += isSeen(xInd, yInd)
        scenicScore(xInd, yInd)
        xInd += 1
    yInd += 1

edgeTrees = len(trees[0])
for y in range(2, len(trees)+1): # IDK why, but this is the only way this works using this loop method
    if y == yLimit:
        edgeTrees += len(trees[0])
        break
    edgeTrees += 2
treesSeen += edgeTrees
print(treesSeen)

print(max(scenicScores))