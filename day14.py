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
    for i in dict:
        print(i, dict[i])
    return dict

def polymerStep(polymerString, pairDict):
    outString = ''
    for i in range(len(polymerString)-1):
        if polymerString[i:i+2] in pairDict:
            outString += polymerString[i:i+1] + pairDict[polymerString[i:i+2]] + polymerString[i:i+1]
        else:
            outString += polymerString[i:i+2]
    return outString

def applySteps(stepNum, startPolymer, pairDict):
    for i in stepNum:
        startPolymer = polymerStep(startPolymer, pairDict)
    return startPolymer

pairDict = createPairDict(pairs)

print(startPolymer)
print(polymerStep(startPolymer, dict))