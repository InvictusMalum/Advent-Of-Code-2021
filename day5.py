f = open("day5input.txt", "r")
input = f.read()

inputs = input.split("\n")

def createPointsList(inputs):
    lines = []
    for input in inputs:
        points = input.split(" -> ")
        p1 = points[0]
        p2 = points[1]

        p1 = p1.split(",")
        p2 = p2.split(",")
        lines.append([[int(p1[0]),int(p1[1])],[int(p2[0]), int(p2[1])]])
    
    return lines

def countOverlappingHorizOrVertLines(lines):
    total = 0
    diagram = [[0 for i in range(1000)] for j in range(1000)]
    for line in lines:
        p1 = line[0]
        p2 = line[1]

        if p1[0] == p2[0] or p1[1] == p2[1]:
            for x in range(min(p1[0],p2[0]), max(p1[0], p2[0])+1):
                for y in range(min(p1[1],p2[1]), max(p1[1], p2[1])+1):
                    diagram[y][x] += 1
        
    for row in range(len(diagram)):
        for col in range(len(diagram[0])):
            if diagram[row][col] > 1:
                total += 1
    return total

def countOverlappingHorizOrVertOr45DegreeLines(lines):
    total = 0
    diagram = [[0 for i in range(1000)] for j in range(1000)]
    for line in lines:
        p1 = line[0]
        p2 = line[1]

        if p1[0] == p2[0] or p1[1] == p2[1]:
            for x in range(min(p1[0],p2[0]), max(p1[0], p2[0])+1):
                for y in range(min(p1[1],p2[1]), max(p1[1], p2[1])+1):
                    diagram[y][x] += 1
                    
        elif p2[0]-p1[0] == p2[1]-p1[1]:
            for add in range(0, max(p2[0]-p1[0], p1[0]-p2[0])+1):
                diagram[min(p1[1],p2[1])+add][min(p1[0],p2[0])+add] += 1
        
        elif p2[0]-p1[0] == -(p2[1]-p1[1]):
            for add in range(0, max(p2[0]-p1[0], p1[0]-p2[0])+1):
                diagram[max(p1[1],p2[1])-add][min(p1[0],p2[0])+add] += 1
        
    for row in range(len(diagram)):
        for col in range(len(diagram[0])):
            if diagram[row][col] > 1:
                total += 1
    return total

print(countOverlappingHorizOrVertLines(createPointsList(inputs)))
print(countOverlappingHorizOrVertOr45DegreeLines(createPointsList(inputs)))