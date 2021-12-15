f = open("day14input.txt", "r")
input = f.read()

sections = input.split("\n\n")

startPolymer = sections[0]
pairs = sections[1].split("\n")

def createPairDict(pairs):
    dict = {}
    for pairCode in pairs:
        pairCode = pairCode.split(" -> ")
        dict[pairCode[0]] = pairCode[1]
    return dict

def polymerStep(polymerString, pairDict):
    outString = ''
    for i in range(len(polymerString)-1):
        if polymerString[i:i+2] in pairDict:
            outString += polymerString[i] + pairDict[polymerString[i:i+2]]
        else:
            outString += polymerString[i]
    outString += polymerString[-1]
    return outString

def applySteps(stepNum, startPolymer, pairDict):
    for i in range(stepNum):
        startPolymer = polymerStep(startPolymer, pairDict)
        print(i)
    return startPolymer

def countLetters(string):
    counts = {}
    for i in string:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    
    return counts

def countMost(string):
    counts = countLetters(string)
    max = 0
    for i in counts:
        if counts[i] > max:
            max = counts[i]
    
    return max

def countLeast(string):
    counts = countLetters(string)
    min = len(string)
    for i in counts:
        if counts[i] < min:
            min = counts[i]

    return min


pairDict = createPairDict(pairs)

startPolymer = applySteps(40, startPolymer, pairDict)
print(countMost(startPolymer) - countLeast(startPolymer))