f = open("day1input.txt", "r")
input = f.read().split("\n")

for i in range(len(input)):
    input[i] = int(input[i])

def countIncreases(input):
    """Counts the number of times two consecutive elements of a list are in ascending order (input[i] < input[i+1])"""
    total = 0
    for i in range(0,len(input)-1):
        if input[i] < input[i+1]:
            total += 1
    return total

def sumAllContiguousGroupsOfThree(input):
    """Sums overlapping groups of three consecutive elements. Sums in a three measurement sliding window. (input[i]+input[i+1]+input[i+2] for every i in list, ending before len(input)-2)"""
    out = []
    for i in range(0,len(input)-2):
        out.append(input[i] + input[i+1] + input[i+2])
    return out

print("Original Increases: " + str(countIncreases(input)))
print("Summed Increases: " + str(countIncreases(sumAllContiguousGroupsOfThree(input))))