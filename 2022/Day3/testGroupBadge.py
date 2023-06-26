# Make a list of each string of letters and find the letter that exists in both halfs.

f = open("testInput.txt", "r")
groups = []
group = []
for x in f:
    x = x.replace("\n", "")
    group.append(x)
    if len(group) == 3:
        groups.append(group)
        group = []

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

def findGroupBadge(group):
    same1 = []
    same2 = []
    for x in group[0]:
        for y in group[1]:
            if x == y:
                same1.append(y)
        for z in group[2]:
            if x == z:
                same2.append(z)
    for i in same1:
        for j in same2:
            if i == j:
                print(f"{i} is the common letter.")
                return i

sum = 0
for group in groups:
    letter = findGroupBadge(group)
    if letter.isupper():
        sum += uppercase[letter]
    else:
        sum += lowercase[letter]
print(f"The sum of all the priorities is {sum}")