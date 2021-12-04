from itertools import zip_longest

# with open('input/i_day4.txt') as file:
#     text = file.read()
#     content = text.splitlines()

with open('input/i_day4test.txt') as file:
    text = file.read()
    #print(text)
    content = text.split("\n")
    #print(content)

    # for line in file:
    #     y = line.split()
    #     print(y)

#put the first element in seperate list
input, rest = [content[0]], content[1:]
#print(input)
#print(rest)
rest = [r.split() for r in rest if r != ""]
#print (cols)
boards = [rest[x:x+5] for x in range(0, len(rest), 5)]
#print(boards)

num = "7"

# print("initial boards")
# for board in boards:
#     print(board)
#     for row in board:
#         print(row)
#         if num in row:
#             row.remove(num)
#             print(row)
#     for i in range(5):
#         cols=[row[i] for row in board]
#         print (cols)
#     # col = list(zip(*board))
#     # colList = [list(c) for c in col]
#     # #print(colList)
#     # for col in colList:
#     #     print(col)


# #check if number is on ANY of the boards
# print("new boards")
# for board in boards:
#     for row in board:
#         row = ["X" for r in row if r == num]

# #print(boards)

# print("new boards")
# for board in boards:
#     print(board)
#     for row in board:
#         print(row)
#     col = list(zip(*board))
#     colList = [list(c) for c in col]
#     #print(colList)
#     for col in colList:
#         print(col)


print("check rows in all boards")
for board in boards:
    print(board)
    for row in board:
        print(row)
        if num in row:
            for i in range(len(row)):
                if row[i] == num:
                    row[i] = "X"
            print(row)
print("board now: ")
print(boards)

print("check cols in all boards")
for board in boards:
    print(board)
    #for row in board:
    for i in range(5):
        cols=[row[i] for row in board]
        print (cols)
