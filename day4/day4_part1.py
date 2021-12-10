with open('input/i_day4.txt') as file:
    text = file.read()
    
    content = text.split("\n")

#put the first element in seperate list
input, rest = content[0].split(","), content[1:]
rest = [r.split() for r in rest if r != ""]
boards = [rest[x:x+5] for x in range(0, len(rest), 5)]


#check if row or col is complete
def checkComplete(inp):
    complete = True
    for i in inp:
        if i != "X":
            complete = False
            break
    return complete


def checkRow(board, num):
    for row in board:
        if num in row:
            for i in range(len(row)):
                if row[i] == num:
                    row[i] = "X"
            result = checkComplete(row)
            if result == True:
                return board
    return False

def checkCol(board, num):
    for i in range(5):
        col=[row[i] for row in board]
        result = checkComplete(col)
        if result == True:
            return board
    return False


print("starting bingo game 1")
winningBoard = None
winningNum = None
for i in input:
    num = i
    if winningBoard == None:
        print("checking for number " + num)
        for board in boards:
            bingoRow = checkRow(board, num)
            if bingoRow == False:
                bingoCol = checkCol(board, num)
                if bingoCol != False:
                    print("Bingo")
                    winningBoard = bingoCol
                    winningNum = num
                    break
            else:
                print("Bingo")
                winningBoard = bingoRow
                winningNum = num
                break

print(winningNum)
print(winningBoard)

remainingNums = [int(n) for group in winningBoard for n in group if n != "X" ]
print(remainingNums)
sumOfRemainingNums = sum(remainingNums)
answer = sumOfRemainingNums * int(winningNum)
print(answer)