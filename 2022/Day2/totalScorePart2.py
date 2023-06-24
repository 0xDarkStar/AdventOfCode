# Read the input file and find out the total score of the player

f = open("input.txt", "r") # Read the input
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

# Due to new information on what the letters mean, the calculations have changed.

totalScore = 0
for i in roundMatrix:
    match i[1]:
        case "X": # Lose
            totalScore += 0
            match i[0]:
                case "A": # Play Scissors
                    totalScore += 3
                case "B": # Play Rock
                    totalScore += 1
                case "C": # Play Paper
                    totalScore += 2
        case "Y": # Draw
            totalScore += 3
            match i[0]:
                case "A": # Play Rock
                    totalScore += 1
                case "B": # Play Paper
                    totalScore += 2
                case "C": # Play Scissors
                    totalScore += 3
        case "Z": # Win
            totalScore += 6
            match i[0]:
                case "A": # Play Paper
                    totalScore += 2
                case "B": # Play Scissors
                    totalScore += 3
                case "C": # Play Rock
                    totalScore += 1
print(totalScore)