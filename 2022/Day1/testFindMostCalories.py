# Testing how to find elf with largest amount of calories
# Turning the matrix into a list by getting the sum of each integer in a sub-list
testList = [[9], [9, 2, 7], [0, 1, 2]] # The matrix

for i in testList: # Grab each sub-list from the main list
    index = testList.index(i) # Get the index of the sub-list
    sum = 0 # To get the sum
    if len(i) == 1: # Does the list have only one item?
        testList[index] = i[0] # It does. Replace that sub-list with the item it has.
        continue # And move on to the next list
    for j in i: # Look at each integer in the sub-list
        sum += j # Add that integer to the sum variable
    testList[index] = sum # All numbers have been added, replace the sub-list with the sum of all items in it.
print(testList) # Shows the list with all the sums
mostCalories = max(testList) # Grabs the highest value from the list
print(mostCalories) # Shows the highest value
