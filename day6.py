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


def fishChildrenInDays(startNum, startDay, totalDays):
    if totalDays-startDay < 8 or (startNum <= 6 and totalDays-startDay < 6):
        print(totalDays)
        return 1
    else:
        print("he")
        total = 1
        for day in range(0,totalDays-startDay):
            if day == startNum or ((day-startNum)%7 == 0 and day > startNum):
                total += fishChildrenInDays(8, startDay + day, totalDays)
        return total
        

def countEndNumInDays(fishLives, days):
    total = 0
    for fish in fishLives:
        total += fishChildrenInDays(fish, 0, days)
    return total


print("Initial Day: "  + str(len(fishLives)))
days = 7
print("After Day " + str(days) + ": " + str(countEndNumInDays(fishLives, days)))

