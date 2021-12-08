f = open("day8input.txt", "r")
input = f.read()

entries = input.split("\n")

def countOnesFoursSevensEights(entries):
    outputs = []
    for entry in entries:
        entry = entry.split(" | ")
        outputs += entry[1].split(" ")
    total = 0
    for output in outputs:
        length = len(output)
        if length in [2,4,3,7]:
            total += 1
    return total

def remove(list, removeList):
    i = 0
    while i < len(list):
        if list[i] in removeList:
            list.pop(i)
            i -= 1
        i += 1
    return list

def getAllConfigs():
    pass

def configurationMakesSense(configuration, allCodes):
    pass

def findConfiguration(notes, outputs):
    allCodes = notes + outputs
    for configuration in notes:
        if configurationMakesSense(configuration, allCodes):
    
def processEntry(entry):
    entry = entry.split(" | ")
    notes = entry[0].split(" ")
    outputs = entry[1].split(" ")

    configuration = findConfiguration(notes, outputs)
   
    number = 0
    return number

def addAllOutputs(entries):
    total = 0
    for entry in entries:
        total += processEntry(entry)
    return total

print(countOnesFoursSevensEights(entries))
processEntry(entries[0])
#print(addAllOutputs(entries))