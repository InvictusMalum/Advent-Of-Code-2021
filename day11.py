from os import dup


f = open("day11input.txt", "r")
input = f.read()

input = input.split("\n")

octopusArray = [[int(input[i][j]) for j in range(len(input[i]))] for i in range(len(input))]

def takeStep(array):
    dupeArray = [[array[i][j] for j in range(len(array[i]))] for i in range(len(array))]
    flashes = 0
    
    # Add one to each
    dupeArray = [[dupeArray[i][j]+1 for j in range(len(dupeArray[i]))] for i in range(len(dupeArray))]
    
    # While there's something > 9
        # Brighten all neighbors
        # Set the 9 to None
    
    greaterThanNines = greaterThanNinesInArray(dupeArray)
    while len(greaterThanNines) != 0:
        greaterThanNines = greaterThanNinesInArray(dupeArray)
        for (i,j) in greaterThanNines:
            for iOff in range(-1,2):
                for jOff in range(-1,2):
                    if i+iOff >= 0 and i+iOff < len(dupeArray) and j+jOff >= 0 and j+jOff < len(dupeArray[0]):
                        if dupeArray[i+iOff][j+jOff] != None:
                            dupeArray[i+iOff][j+jOff] += 1
            dupeArray[i][j] = None
            flashes += 1
                            
    # Set all Nones to 0
    for i in range(len(dupeArray)):
        for j in range(len(dupeArray[i])):
            if dupeArray[i][j] == None:
                dupeArray[i][j] = 0
    
    return flashes, dupeArray

def greaterThanNinesInArray(array):
    out = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] != None and array[i][j] > 9:
                out.append((i,j))
    return out

def countFlashesInSteps(array, steps):
    flashes = 0
    for i in range(steps):
        output = takeStep(array)
        flashes += output[0]
        array = output[1]
    return flashes

def isAllZero(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] != 0:
                return False
    return True
            

def countStepOfSynchronized(array):
    step = 0
    sync = False
    while sync != True:
        step += 1
        array = takeStep(array)[1]
        sync = isAllZero(array)
    return step
    

print(countFlashesInSteps(octopusArray, 100))
print(countStepOfSynchronized(octopusArray))