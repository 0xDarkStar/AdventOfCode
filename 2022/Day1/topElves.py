# Purpose: Find the amount of calories the top three elves hold.

f = open("Matrix.txt", "r") # Reopen the file, but read it this time
content = f.read() # Grab the matrix
print(content)
elfList = eval(content) # Use eval to turn the string matrix into an actual matrix

for i in elfList: # Grab each sub-list from the main list
    index = elfList.index(i) # Get the index of the sub-list
    sum = 0 # To get the sum
    if len(i) == 1: # Does the list have only one item?
        elfList[index] = i[0] # It does. Replace that sub-list with the item it has.
        continue # And move on to the next list
    for j in i: # Look at each integer in the sub-list
        sum += j # Add that integer to the sum variable
    elfList[index] = sum # All numbers have been added, replace the sub-list with the sum of all items in it.

mostCalories = max(elfList) # Grabs the highest value from the list
print(mostCalories) # Shows the highest value
elfList.remove(mostCalories)

mostCalories2 = max(elfList) # Grabs the highest value from the list
print(mostCalories2) # Shows the highest value
elfList.remove(mostCalories2)

mostCalories3 = max(elfList) # Grabs the highest value from the list
print(mostCalories3) # Shows the highest value
elfList.remove(mostCalories3)

sum = mostCalories + mostCalories2 + mostCalories3
print(sum)