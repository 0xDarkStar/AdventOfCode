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


totalScore = 0
for i in roundMatrix:
    match i[1]:
        case "X": # Rock
            totalScore += 1
            match i[0]:
                case "A": # Draw
                    totalScore += 3
                case "B": # Lose
                    continue
                case "C": # Win
                    totalScore += 6
        case "Y": # Paper
            totalScore += 2
            match i[0]:
                case "A": # Win
                    totalScore += 6
                case "B": # Draw
                    totalScore += 3
                case "C": # Lose
                    continue
        case "Z": # Scissors
            totalScore += 3
            match i[0]:
                case "A": # Lose
                    continue
                case "B": # Win
                    totalScore += 6
                case "C": # Draw
                    totalScore += 3
print(totalScore)