f = open("day10input.txt", "r")
input = f.read()

lines = input.split("\n")
# (, [, {, <
startCharacters = ['(','[','{','<']
endCharacters =   [')',']','}','>']

def findCorruptionError(line):
    open = []
    for char in line:
        if char in startCharacters:
            open.append(char)
        else:
            if startCharacters[endCharacters.index(char)] == open[-1]:
                open.pop(-1)
            else:
                return char
    return None

def findAllCorruptions(lines):
    errors = {}
    endCharacters = [')',']','}','>', None]
    for character in endCharacters:
        errors[character] = 0
    for line in lines:
        errors[findCorruptionError(line)] += 1
    
    return errors

def sumAllErrorCodes(errors, values):
    total = 0
    for value in values:
        total += errors[value] * values[value]
    return total
        
print(sumAllErrorCodes(findAllCorruptions(lines), {')':3,']':57,'}':1197,'>':25137}))


def sortOutCorrupted(lines):
    outLines = []
    for line in lines:
        if findCorruptionError(line) == None:
            outLines.append(line)
    return outLines

def reverseOpen(open):
    out = []
    for i in range(len(open)-1, -1,-1):
        out.append(endCharacters[startCharacters.index(open[i])])
    return out

def autocomplete(line):
    open = []
    for char in line:
        if char in startCharacters:
            open.append(char)
        else:
            if startCharacters[endCharacters.index(char)] == open[-1]:
                open.pop(-1)
    return reverseOpen(open)

def autocompleteAllLines(lines):
    autocompletes = []
    for line in lines:
        if autocomplete(line) != None:
            autocompletes.append(autocomplete(line))
    return autocompletes

def getAutoCompleteScore(list, values):
    total = 0
        
    for char in list:
        total *= 5
        total += values[char]
    return total

def scoreAllAutoCompletes(completes, values):
    out = []
    for complete in completes:
        out.append(getAutoCompleteScore(complete, values))
    return out

def findMiddleOfListWhenSorted(list):
    list.sort()
    return list[len(list)//2]

linesWithoutCorruptions = sortOutCorrupted(lines)
print(findMiddleOfListWhenSorted(scoreAllAutoCompletes(autocompleteAllLines(linesWithoutCorruptions),{')':1,']':2,'}':3,'>':4})))
