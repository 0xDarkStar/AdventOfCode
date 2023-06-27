# This file is the one used to find the answer

# This function checks if one range of numbers is in another
def pairInPair(pairs, times):
    count = 0 # How many numbers are in the other range
    if len(pairs[1]) <= len(pairs[0]): # The second pair is smaller or the same size as the first pair
        for i in pairs[1]: # Cycle through the numbers in the second pair
            for j in pairs[0]: # Cycle through the numbers in the first pair
                if i == j: # The two numbers are the same
                    count += 1 # Add 1 to the count
                    break # Move to the next number
        if count == len(pairs[1]): # All of the numbers in the second pair are in the first pair
            times += 1 # Add 1 to the amount of times they were in each other
            return times # Return
        else: # Not all of the numbers from the second pair are in the first
            return times # Return
    else: # The first pair is bigger
        for i in pairs[0]: # Cycle through the numbers in the first pair
            for j in pairs[1]: # Cycle throught he numbers in the second pair
                if i == j: # The two numbers are the same
                    count += 1 # Add 1 to the count
                    break # Move to the next number
        if count == len(pairs[0]): # All of the numbers in the first pair are in the second pair
            times += 1 # Add 1 to the amount of times they were in each other
            return times # Return
        else: # Not all of the numbers from the first pair are in the second
            return times # Return
        
# This function makes a list and puts the numbers in the range specified into said list
def makeListRange(pair):
    end = pair[0].index("-") # Find out where to split the two numbers apart for the first range
    x1 = int(pair[0][0:end]) # Grab the starting number
    x2 = int(pair[0][end+1:]) # Grab the final number
    xList = [] # Make the list to store the range
    for a in range(x1, x2+1): # Go through the numbers
        xList.append(a) # Add them to the list
    end = pair[1].index("-") # Find out where to split the two numbers apart for the second range
    y1 = int(pair[1][0:end]) # Grab the starting number
    y2 = int(pair[1][end+1:]) # Grab the final number
    yList = [] # Make the list to store the range
    for a in range(y1, y2+1): # Go through the numbers
        yList.append(a) # Add them to the list
    pairList = [xList, yList] # Put the two ranges into their own list
    return pairList # Return the list


f = open("input.txt", "r") # Get the ranges from the file
pairsList = [] # Make the list to store them
for x in f:
    x = x.replace("\n", "") # Remove the newline character
    templist = list(x.split(",")) # Separate the two ranges but keep them in the same list
    pairsList.append(templist) # Put that list into the other list
times = 0 # To count how many times a range was in another
for x in pairsList: # Grab the pairs of ranges
    pair = makeListRange(x) # Get the ranges in list form
    times = pairInPair(pair, times) # Check if they are in one another
print(times) # Say how many times a range was in another