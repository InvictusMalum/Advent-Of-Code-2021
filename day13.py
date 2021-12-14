from os import dup


f = open("day13input.txt", "r")
input = f.read()

sections = input.split("\n\n")

onIndexes = sections[0].split("\n")
folds = sections[1].split("\n")

def createArray(onIndexes):
    xValues = []
    yValues = []
    for point in onIndexes:
        point = point.split(",")
        xValues.append(int(point[0]))
        yValues.append(int(point[1]))

    array = [[False for j in range(max(xValues)+1)] for i in range(max(yValues)+1)]
    for point in onIndexes:
        point = point.split(",")
        x = int(point[0])
        y = int(point[1])
        
        array[y][x] = 1
    return array

def horizontalFold(array, yLine):
    dupeArray = [[array[i][j] for j in range(len(array[i]))] for i in range(yLine)]

    for i in range(yLine+1, len(array)):
        for j in range(len(array[0])):
            if array[i][j]:
                dupeArray[2*yLine-i][j] = True

    return dupeArray

def verticalFold(array, xLine):
    dupeArray = [[array[i][j] for j in range(xLine)] for i in range(len(array))]

    for i in range(len(array)):
        for j in range(xLine+1, len(array[0])):
            if array[i][j]:
                dupeArray[i][2*xLine-j] = True
            
    return dupeArray

def runThroughDirection(array, command):
    command = command.split(" ")[2]
    splitCommand = command.split("=")
    if splitCommand[0] == 'x':
        array = verticalFold(array, int(splitCommand[1]))
    else:
        array = horizontalFold(array, int(splitCommand[1]))
    return array

def allFolds(startArray, commands):
    for command in commands:
        startArray = runThroughDirection(startArray, command)
    return startArray

def countOnes(array):
    total = 0
    for i in array:
        for j in i:
            if j:
                total += 1
    return total

def printFormattedArray(array):
    for row in array:
        for value in row:
            if value:
                print("# ", end = '')
            else:
                print('  ', end = '')
        print("")

array = createArray(onIndexes)
array = runThroughDirection(array, folds[0])
print(countOnes(array))

array = createArray(onIndexes)
array = allFolds(array, folds)
printFormattedArray(array)
print(countOnes(array))
