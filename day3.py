f = open("day3input.txt", "r")
input = f.read()

numberStrings = input.split("\n")
# Gamma Rate
def mostCommonAtPosN(n, strings):
    counts = {'0':0, '1':0}
    for string in strings:
        counts[string[n]] += 1
    if counts['0'] > counts['1']:
        return '0'
    else:
        return '1'

def getGamma(numberStrings):
    gamma = ''
    for n in range(len(numberStrings[0])):
        gamma += mostCommonAtPosN(n, numberStrings)
    return gamma


# Epsilon Rate
# Count just bitwise not the Gamma rate but wrote it out just in case part 2 gets funky
def leastCommonAtPosN(n, strings):
    counts = {'0':0, '1':0}
    for string in strings:
        counts[string[n]] += 1
    if counts['0'] > counts['1']:
        return '1'
    else:
        return '0'

def getEpsilon(numberStrings):
    epsilon = ''
    for n in range(len(numberStrings[0])):
        epsilon += leastCommonAtPosN(n, numberStrings)
    return epsilon

def binaryStringToDecimal(string):
    return int(string, 2)

print(binaryStringToDecimal(getGamma(numberStrings)) * binaryStringToDecimal(getEpsilon(numberStrings)))




# Life support = O2 gen rating * CO2 scrubber rating 

def FindRating(numberStrings, criteriaFunction):
    dupeNumberStrings = []
    for string in numberStrings:
        dupeNumberStrings.append(string) 
    
    for n in range(len(dupeNumberStrings[0])):
        keepBit = criteriaFunction(n, dupeNumberStrings)
        i = 0
        while i < len(dupeNumberStrings) and len(dupeNumberStrings) > 1:
            if dupeNumberStrings[i][n] != keepBit:
                dupeNumberStrings.pop(i)
                i -= 1
            i += 1
    return dupeNumberStrings
O2GenRating = binaryStringToDecimal(FindRating(numberStrings, mostCommonAtPosN)[0])
CO2ScrubberRating = binaryStringToDecimal(FindRating(numberStrings, leastCommonAtPosN)[0])

print(O2GenRating*CO2ScrubberRating)
