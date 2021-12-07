import statistics

f = open("day7input.txt", "r")
input = f.read()

positions = [int(i) for i in input.split(",")]

# Cost = Steps
def totalDeviation(positions, number):
    total = 0
    for position in positions:
        total += abs(number-position)
    return total

def costOfStep(step):
    return step*(step+1)//2

def totalFuelForIncreasingCost(positions, number):
    total = 0
    for position in positions:
        total += costOfStep(abs(number-position))
    return total


deviations = []
for i in range(max(positions)):
    deviations.append(totalDeviation(positions, i))

print(min(deviations))


deviations = []
for i in range(max(positions)):
    deviations.append(totalFuelForIncreasingCost(positions, i))

print(min(deviations))
