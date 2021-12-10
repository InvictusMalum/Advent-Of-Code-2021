f = open("day9input.txt", "r")
input = f.read()

input = input.split("\n")

# Part 1
def getAllLowPoints(input):
    lowPoints = []
    for i in range(len(input)):
        for j in range(len(input[i])):
            neighbors = []
            for (iOff, jOff) in [(1,0),(-1,0),(0,-1),(0,1)]:
                if i + iOff >= 0 and i + iOff < len(input) and j + jOff >= 0 and j + jOff < len(input[i]):
                    neighbors.append(int(input[i+iOff][j+jOff]))
            
            isLowPoint = True
            for item in neighbors:
                if item <= int(input[i][j]):
                    isLowPoint = False
            
            if isLowPoint:
                lowPoints.append(int(input[i][j]))
    return lowPoints


# Part 2
def getAllLowPointsIndexes(input):
    lowPointsIndexes = []
    for i in range(len(input)):
        for j in range(len(input[i])):
            neighbors = []
            for (iOff, jOff) in [(1,0),(-1,0),(0,-1),(0,1)]:
                if i + iOff >= 0 and i + iOff < len(input) and j + jOff >= 0 and j + jOff < len(input[i]):
                    neighbors.append(int(input[i+iOff][j+jOff]))
            
            isLowPoint = True
            for item in neighbors:
                if item <= int(input[i][j]):
                    isLowPoint = False
            
            if isLowPoint:
                lowPointsIndexes.append((i,j))
    return lowPointsIndexes

def findBasinSize(groundMap, point):
    total = 0
    i = point[0]
    j = point[1]
    for (iOff, jOff) in [(1,0),(-1,0),(0,-1),(0,1)]:
        if i + iOff >= 0 and i + iOff < len(input) and j + jOff >= 0 and j + jOff < len(input[i]):
            if int(groundMap[i+iOff][j+jOff]) > int(groundMap[i][j]):
                if int(groundMap[i+iOff][j+jOff]) < 9:
                    total += 1 + findBasinSize(groundMap, (i+iOff,j+jOff))
    return total

def findAllBasinSizes(groundMap, lowPoints):
    basinSizes = {}
    for point in lowPoints:
        basinSizes[point] = findBasinSize(groundMap, point)
    return basinSizes

def findThreeLargest(dictionary):
    largest = [0,0,0]
    for x in dictionary:
        if dictionary[x] > min(largest):
            largest.remove(min(largest))
            largest.append(dictionary[x])
    return largest

print(sum(getAllLowPoints(input)) + len(getAllLowPoints(input)))

largestBasins = findThreeLargest(findAllBasinSizes(input, getAllLowPointsIndexes(input)))
print(largestBasins)
print(largestBasins[0]*largestBasins[1]*largestBasins[2])