f = open("day18input.txt", "r")
input = f.read()

lines = input.split("\n")


def addTwo(string1, string2):
    return '[' + string1 + ',' + string2 + ']'

def explode(string):
    open = 0
    i = 0
    while i < len(string):
        if string[i] == '[' and open >= 4:
            list = [string[:i], string[i:][string.index(']')+1:]]
            nextStart = string[i:].index(']')+1+i
            nums = string[i+1:string.index(']')].split(",")[:2]
            print(nums)
            string = rightMostAdd(list[0], int(nums[0])) + '0' + leftMostAdd(list[1], int(nums[1]))
            i = nextStart
        elif string[i] == '[':
            open += 1
        elif string[i] == ']':
            open -= 1
        i += 1
    return string

def rightMostAdd(string, num):
    return string

def leftMostAdd(string, num):
    return string

print(explode('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]'))
        
