f = open("day15input.txt", "r")
input = f.read()

input = input.split("\n")

riskMap = [[int(input[i][j]) for j in range(len(input[i]))] for i in range(len(input))]

neighborOffsets = []
for i in range(-1,2):
    for j in range(-1,2):
        neighborOffsets.append((i,j))
neighborOffsets.remove((0,0))

def traverseMap(riskMap, start = (0,0), end = (len(riskMap[0])-1, len(riskMap)-1)):
    nodeCosts = [[None for j in range(len(riskMap[0]))] for i in range(len(riskMap))]

    neighbors = [(0,-1),(0,1),(-1,0),(1,0)]
    # Arbitrary repeat, would only be needed if you dont start at 0,0. Could make a check but it's not needed for the problem
    for a in range(10):
        nodeCosts[start[0]][start[1]] = 0
        for i in range(len(nodeCosts)):
            for j in range(len(nodeCosts[i])):
                for offset in neighbors:
                    if i+offset[0] >= 0 and i+offset[0] < len(riskMap) and j+offset[1] >= 0 and j+offset[1] < len(riskMap[0]) and nodeCosts[i+offset[0]][j+offset[1]] != None:
                        if nodeCosts[i][j] == None or nodeCosts[i+offset[0]][j+offset[1]] + riskMap[i][j] < nodeCosts[i][j]:
                            nodeCosts[i][j] = nodeCosts[i+offset[0]][j+offset[1]] + riskMap[i][j]
    
    return nodeCosts

print(traverseMap(riskMap)[-1][-1])

def addAndWrap(number, addValue):
    return (number + addValue - 1) % 9 + 1

def createLargeMap(riskMap):
    largeMap = [[riskMap[i%len(riskMap)][j%len(riskMap[0])] for j in range(len(riskMap[0])*5)] for i in range(len(riskMap)*5)]

    chunkHeight = len(riskMap)
    chunkWidth = len(riskMap[0])

    for chunkI in range(0,5):
        for chunkJ in range(0,5):
            for i in range(chunkI*chunkHeight, chunkI*chunkHeight+chunkHeight):
                for j in range(chunkJ*chunkWidth, chunkJ*chunkWidth+chunkWidth):
                    largeMap[i][j] = addAndWrap(largeMap[i][j], chunkI+chunkJ)
    return largeMap
    
print(traverseMap(createLargeMap(riskMap))[-1][-1])
