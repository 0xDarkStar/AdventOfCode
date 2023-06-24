# Purpose: Read the input file and make the matrix that the rest of the scripts work on.

f = open("testInput.txt", "r") # Read the input
fileLines = [] # Make a list to store the rounds (string)
for x in f:
    fileLines.append(x) # Add each round (string) to the list

roundMatrix = [] # Make a list to store each round (list)
for i in fileLines: # Look at each round (string)
    tempList = [] # Make a temporary list to store the two choices
    opponent = i[0] # Get the opponent's choice
    player = i[2] # Get the player's choice
    tempList.append(opponent) # Add the opponent's choice to the temporary list
    tempList.append(player) # Add the player's choice to the temporary list
    roundMatrix.append(tempList) # Add the temporary list to the main list, now matrix.
print(roundMatrix) # Look at the matrix

# Would've been easier to do Day 1's input like this.