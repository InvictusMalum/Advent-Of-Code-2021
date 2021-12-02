f = open("day2input.txt", "r")
input = f.read()

input = input.split("\n")

def runThroughCourseP1(course):
    horiz = 0
    depth = 0
    for instruction in course:
        splitInst = instruction.split(" ")
        direction = splitInst[0]
        steps = int(splitInst[1])

        if direction == "forward":
            horiz += steps
        elif direction == "up":
            depth -= steps
        elif direction == "down":
            depth += steps
    return horiz * depth

def runThroughCourseP2(course):
    horiz = 0
    depth = 0
    aim = 0
    for instruction in course:
        splitInst = instruction.split(" ")
        direction = splitInst[0]
        steps = int(splitInst[1])

        if direction == "forward":
            horiz += steps
            depth += aim * steps
        elif direction == "up":
            aim -= steps
        elif direction == "down":
            aim += steps
    return horiz * depth

print(runThroughCourseP1(input))
print(runThroughCourseP2(input))