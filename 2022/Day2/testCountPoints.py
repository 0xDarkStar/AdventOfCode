# Purpose: Read the matrix that was made and find out how many points the player got.

roundMatrix = [["A", "Y"], ["B", "Z"], ["C", "X"]]

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