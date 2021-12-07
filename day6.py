f = open("day6input.txt", "r")
input = f.read()

fishLives = input.split(",")
for i in range(len(fishLives)):
    fishLives[i] = int(fishLives[i])

def runADay(fishLives):
    for i in range(len(fishLives)):
        fishLives[i] -= 1
        if fishLives[i] == -1:
            fishLives[i] = 6
            fishLives.append(8)
    return fishLives


def fishChildrenInDays(startNum, parentMax, startingMax, totalDays):
    numbers = parentMax + 1
    offsets = [0 for i in range(numbers)]
    offsets[startNum] = 1

    spawnStorage = [0 for i in range(numbers)]

    for day in range(totalDays+startingMax-parentMax):
        spawnStorage[(day+startingMax-parentMax)%numbers] += offsets[day%numbers]
        offsets[day%numbers] += spawnStorage[day%numbers]
        spawnStorage[day%numbers] = 0

    return sum(offsets) 
        

def countEndNumInDays(fishLives, days):
    total = 0
    for fish in fishLives:
        total += fishChildrenInDays(fish, 6, 8, days)
    return total


print("Initial Day: "  + str(len(fishLives)))
days = 256
print("After Day " + str(days) + ": " + str(countEndNumInDays(fishLives, days)))

