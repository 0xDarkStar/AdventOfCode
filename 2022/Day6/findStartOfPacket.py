f = open("input.txt", "r")
inputs = []
for x in f:
    x = x.replace("\n", "")
    inputs.append(x)

def find_repeats(myList):
    found = [] # To store the distinct characters
    howLong = 0 # To know how long it took
    for a in myList:
        if len(found) == 4: # found four distinct characters
            break # We win!
        elif a in found: # Our character is in the list already
            indexOfA = found.index(a) # Find out where it is in the list
            for b in range(indexOfA+1): # Go through the list, all the way to the character we're at
                found[b] = 9 # Turn it into 9
            while 9 in found: # Look for all the 9s in the list
                found.remove(9) # Remove them
            found.append(a) # Add our character now
        else:
            found.append(a) # Add our character to the list
        howLong += 1 # Got the letter
    print(howLong) # Print how many letters we had to go through
    print(found) # Print the list of letters

for x in inputs: # Cycle through each line of inputs (there's only one)
    inputList = [] # Make an empty list for the characters in the line
    for y in x: # Grab each character from the line
        inputList.append(y) # Add the character to the list
    find_repeats(inputList) # Find the marker