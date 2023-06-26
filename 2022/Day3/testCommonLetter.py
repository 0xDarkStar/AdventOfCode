# Make a list of each string of letters and find the letter that exists in both halfs.

f = open("testInput.txt", "r")
fileLines = []
for x in f:
    x = x.replace("\n", "")
    fileLines.append(x)

lowercase = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26
}

uppercase = {
    "A": 27,
    "B": 28,
    "C": 29,
    "D": 30,
    "E": 31,
    "F": 32,
    "G": 33,
    "H": 34,
    "I": 35,
    "J": 36,
    "K": 37,
    "L": 38,
    "M": 39,
    "N": 40,
    "O": 41,
    "P": 42,
    "Q": 43,
    "R": 44,
    "S": 45,
    "T": 46,
    "Y": 47,
    "V": 48,
    "W": 49,
    "X": 50,
    "Y": 51,
    "Z": 52
}

ignore = []

def removeFromIgnore(letter):
    count = 0
    for x in ignore:
        if x == letter:
            count += 1
            if count == 3:
                a = 0
                while a < 3:
                    ignore.remove(letter)
                    a += 1
                return True
    return False

def findCommonLetter(package):
    length = len(package)
    midpoint = int(length/2)
    half1 = package[0:midpoint]
    half2 = package[midpoint:]
    for i in half1:
        for j in half2:
            if i == j:
                print(f"The common letter in {package} is {i}.", end="")
                if i.isupper():
                    print(f" It has a priority of {uppercase[i]}.")
                    if i in ignore:
                        if removeFromIgnore(i):
                            ignore.append(i)
                            return uppercase[i]
                        else:
                            ignore.append(i)
                            return 0
                    else:
                        ignore.append(i)
                        return uppercase[i]
                else:
                    print(f" It has a priority of {lowercase[i]}.")
                    
                    if i in ignore:
                        if removeFromIgnore(i):
                            ignore.append(i)
                            return lowercase[i]
                        else:
                            ignore.append(i)
                            return 0
                    else:
                        ignore.append(i)
                        return lowercase[i]

sum = 0
for a in fileLines:
    sum += findCommonLetter(a)
print(f"The sum of all the priorities is {sum}")