from re import search

f = open("testInput.txt", "r") # Reads the input file
fileLines = [] # To store each line from the file
for x in f:
    fileLines.append(x) # Puts each line into the list

f = open("testMatrix.txt", "w") # Makes a file to make a matrix
f.write("[[") # Start of the matrix
previous = "[" # Tell it what was last there
for x in fileLines: # Start adding more items, lists, whatever, to the matrix.
    if x == "\n":
        f.write("]")
        previous = "]"
    elif previous == "[":
        x = x.replace("\n", "")
        f.write(x)
        previous = x
    elif search(".[0-9]", previous):
        x = x.replace("\n", "")
        f.write(f", {x}")
        previous = x
    else:
        x = x.replace("\n", "")
        f.write(f", [{x}")
        previous = x
f.write("]]") # End of the matrix
f.close() # Close the file

f = open("testMatrix.txt", "r") # Reopen the file, but read it this time
content = f.read() # Grab the matrix
elfList = eval(content) # Use eval to turn the string matrix into an actual matrix
print(elfList) # Show the matrix

for i in elfList: # Grab each sub-list from the main list
    index = elfList.index(i) # Get the index of the sub-list
    sum = 0 # To get the sum
    if len(i) == 1: # Does the list have only one item?
        elfList[index] = i[0] # It does. Replace that sub-list with the item it has.
        continue # And move on to the next list
    for j in i: # Look at each integer in the sub-list
        sum += j # Add that integer to the sum variable
    elfList[index] = sum # All numbers have been added, replace the sub-list with the sum of all items in it.
print(elfList) # Shows the list with all the sums
mostCalories = max(elfList) # Grabs the highest value from the list
print(mostCalories) # Shows the highest value