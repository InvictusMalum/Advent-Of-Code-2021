f = open("day18input.txt", "r")
input = f.read()

lines = input.split("\n")

class SnailHolder():
    snails = []
    allSnails = []

    def populateAllSnails():
        SnailHolder.allSnails = []
        for primarySnail in SnailHolder.snails:
            for snail in primarySnail.getChildren():
                if type(snail) is Snailfish:
                    SnailHolder.allSnails.append(snail)

    def reduceAll():
        for snail in SnailHolder.allSnails:
            snail.explodeIfNested()

class Snailfish():
    def __init__(self, sF1 = None, sF2 = None, parent = SnailHolder):
        self.snails = [Snailfish.createSnailFish(sF1, self), Snailfish.createSnailFish(sF2, self)]
        self.parent = parent
        if parent == SnailHolder:
            SnailHolder.snails.append(self)

    def __add__(self, other):
        other.parent.snails.remove(other)
        self.parent.snails.remove(self)
        return Snailfish.createSnailFish('[' + str(self) + ',' + str(other) + ']', self.parent)
    
    def __str__(self):
        return '[' + str(self.snails[0]) + ',' + str(self.snails[1]) + ']'

    def getChildren(self):
        out = []
        for snail in self.snails:
            if type(snail) is Snailfish:
                out.append(snail)
                for child in snail.snails:
                    out.append(child)
        return out

    def createSnailFish(string, parent = SnailHolder):
        if ',' not in string:
            return int(string)
        elif '[' in string:
            string = string[1:-1]
            leftCount = 0
            rightCount = 0
            for index in range(len(string)):
                if string[index] == ',' and leftCount == rightCount:
                    return Snailfish(string[:index], string[index+1:], parent)
                elif string[index] == '[':
                    leftCount += 1
                elif string[index] == ']':
                    rightCount += 1

    def countParents(self):
        parent = self.parent
        self.parents = 0
        while parent != SnailHolder:
            self.parents += 1
            parent = parent.parent

for line in lines:
    Snailfish.createSnailFish(line)

Snail = Snailfish.createSnailFish('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]')

SnailHolder.populateAllSnails()
