f = open("day12input.txt", "r")
input = f.read()

pathCodes = input.split("\n")

def pathDictAndCavesList(pathCodes):
    paths = {}
    caves = []
    
    for createCommand in pathCodes:
        points = createCommand.split("-")
        if points[0] not in caves:
            caves.append(points[0])
            paths[points[0]] = []
        if points[1] not in caves:
            caves.append(points[1])
            paths[points[1]] = []
        
        paths[points[0]].append(points[1])
        paths[points[1]].append(points[0])

    return paths, caves

def isSmallCave(cave):
    if cave.lower() == cave:
        return True
    return False

def pathsToEnd(pathsDict, start):
    if start == 'end':
        return 'end'
    else:
        paths = []
        for element in pathsDict[start]:
            for path in pathsToEnd(pathsDict, element):
                paths.append(['start'] + path)

paths, caves = pathDictAndCavesList(pathCodes)
print(pathsToEnd(paths, 'start'))