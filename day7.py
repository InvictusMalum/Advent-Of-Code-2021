import statistics

f = open("day7input.txt", "r")
input = f.read()

positions = [int(i) for i in input.split(",")]

def totalDeviation(positions, number):
    total = 0
    for position in positions:
        total += abs(number-position)
    return total

deviations = []
for i in range(max(positions)):
    deviations.append(totalDeviation(positions, i))

print(min(deviations))
