f = open("day4input.txt", "r")
input = f.read()

input = input.split("\n")

def separateInput(input):
    numbers = ""
    boards = []
    
    # 0 = numbers
    # From then on, nowOn-1 = boardIndex
    nowOn = 0
    board = []
    for i in range(len(input)):
        if input[i] == '':
            nowOn += 1
        elif nowOn == 0:
            numbers = input[i]
        else:
            board.append(input[i])
            if i+1 == len(input) or input[i+1] == '':
                boards.append(board)
                board = []
    return numbers, boards

def removeAll(list, string):
    while string in list:
        list.remove(string)
    return list

def processNumbersAndBoards(numbers, boards):
    numbers = numbers.split(',')
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

    boards = [[removeAll(boardRow.split(" "),'') for boardRow in board] for board in boards]

    for i in range(len(boards)):
        for j in range(len(boards[i])):
            for k in range(len(boards[i][j])):
                boards[i][j][k] = int(boards[i][j][k])
    
    return numbers, boards

def wonBoard(board):
    for row in range(len(board)):
        thisRow = True
        for col in range(len(board[0])):
            if board[row][col] != -1:
                thisRow = False
        if thisRow:
            return True
    
    for col in range(len(board[0])):
        thisCol = True
        for row in range(len(board)):
            if board[row][col] != -1:
                thisCol = False
        if thisCol:
            return True
    return False
        
def totalOfBoard(board):
    total = 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != -1:
                total += board[row][col]
    return total

def playMove(number, board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == number:
                board[i][j] = -1
            if wonBoard(board):
                return totalOfBoard(board) * number
    return -1

def playAllBingosAndStopAtWin(numbers, boards):
    for number in numbers:
        for board in boards:
            out = playMove(number, board)
            if out != -1:
                return out

def findLastWin(numbers, boards):
    for number in numbers:
        for board in boards:
            out = playMove(number, board)
            if out != -1:
                boards.remove(board)
                if len(boards) == 1:
                    return out
            

numbers, boards = separateInput(input)
numbers, boards = processNumbersAndBoards(numbers, boards)
print(playAllBingosAndStopAtWin(numbers, boards))
print(findLastWin(numbers, boards))