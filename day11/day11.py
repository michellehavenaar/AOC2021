with open("day11/i_day11test.txt") as f:
    text = f.read()

data = text.split("\n")
data = [list(d) for d in data]
# print(data)

grid = []
for d in data:
    row = [int(el) for el in d]
    grid.append(row)
print(grid)

row = len(grid)
col = len(grid[0])
flashCounter = 0

# def incFromNeighbours(x, y, flashCounter):
#     # nort west = x-1, y-1
#     if y - 1 >= 0:
#         # north = x, y-1
#         neighbour = grid[x][y-1]
#         if neighbour == 10:
#             grid[x][y] +=1
#             if grid[x][y] == 10:
#                 flashCounter +=1
#     if x + 1 < len(grid[0])-1 and y - 1 >= 0:
#         # north east = x+1, y-1
#         neighbour = grid[x + 1][y - 1]
#         if neighbour == 10:
#             grid[x][y] +=1
#             if grid[x][y] == 10:
#                 flashCounter +=1
#     if x + 1 < len(grid[0])-1:
#         # east = x+1, y
#         neighbour = grid[x + 1][y]
#         if neighbour == 10:
#             grid[x][y] +=1
#             if grid[x][y] == 10:
#                 flashCounter +=1
#     if x + 1 < len(grid[0])-1 and y + 1 < len(grid) -1:
#         # south east = x+1, y+1
#         neighbour = grid[x + 1][y + 1]
#         if neighbour == 10:
#             grid[x][y] +=1
#             if grid[x][y] == 10:
#                 flashCounter +=1
#     if y + 1 < len(grid)-1:
#         # south = x, y+1
#         neighbour = grid[x][y + 1]
#         if neighbour == 10:
#             grid[x][y] +=1
#             if grid[x][y] == 10:
#                 flashCounter +=1
#     if x - 1 <= 0 and y + 1 < len(grid)-1:
#         # south west = x-1, y+1
#         neighbour = grid[x - 1][y + 1]
#         if neighbour == 10:
#             grid[x][y] +=1
#             if grid[x][y] == 10:
#                 flashCounter +=1
#     if x - 1 <= 0:
#         # west = x-1, y
#         neighbour = grid[x - 1][y]
#         if neighbour == 10:
#             grid[x][y] +=1
#             if grid[x][y] == 10:
#                 flashCounter +=1
#     if x - 1 <= 0 and y - 1 >= 0:
#         # north west = x-1, y-1
#         neighbour = grid[x - 1][y - 1]
#         if neighbour == 10:
#             grid[x][y] +=1
#             if grid[x][y] == 10:
#                 flashCounter +=1

# grid = [[2, 2, 2, 2, 2], [2, 10, 10, 10, 2], [2, 10, 2, 10, 2], [2, 10, 10, 10, 2], [2, 2, 2, 2, 2]]
# x = 0
# y = 0
# if x + 1 < len(grid[0])-1 and y + 1 < len(grid) -1:
#     print("true")
#     neighbour = grid[x + 1][y + 1]
#     print(neighbour)
#     if neighbour == 10:
#         grid[x][y] +=1
# else:
#     print("false")

# print(grid)
# x = 2
# y = 2
# if x - 1 >= 0 and y + 1 <= len(grid)-1:
#     print("true")
# else: 
#     print("false")

for step in range(1, 3):
    print("step: " + str(step))

    #step 1
    for i in range(row):
        for j in range(col):
            x = i
            y = j
            # value = grid[x][y]
            grid[x][y] +=1
            if grid[x][y] == 10:
                flashCounter +=1

    print(grid)
    print(flashCounter)

    #step 2
    for i in range(row):
        for j in range(col):
            x = i
            y = j
            # print(x,y)
            if grid[x][y] != 10:
                if y - 1 >= 0:
                    # print("N")
                    # north = x, y-1
                    neighbour = grid[x][y-1]
                    if neighbour == 10:
                        grid[x][y] +=1
                        if grid[x][y] == 10:
                            flashCounter +=1
                if x + 1 < len(grid[0])-1 and y - 1 >= 0:
                    # north east = x+1, y-1
                    # print("NE")
                    neighbour = grid[x + 1][y - 1]
                    if neighbour == 10:
                        grid[x][y] +=1
                        if grid[x][y] == 10:
                            flashCounter +=1
                if x + 1 < len(grid[0])-1:
                    # east = x+1, y
                    # print("E")
                    neighbour = grid[x + 1][y]
                    if neighbour == 10:
                        grid[x][y] +=1
                        if grid[x][y] == 10:
                            flashCounter +=1
                if x + 1 < len(grid[0])-1 and y + 1 < len(grid) -1:
                    # south east = x+1, y+1
                    # print("SE")
                    neighbour = grid[x + 1][y + 1]
                    if neighbour == 10:
                        grid[x][y] +=1
                        if grid[x][y] == 10:
                            flashCounter +=1
                if y + 1 <= len(grid)-1:
                    # south = x, y+1
                    # print("S")
                    neighbour = grid[x][y + 1]
                    if neighbour == 10:
                        grid[x][y] +=1
                        if grid[x][y] == 10:
                            flashCounter +=1
                if x - 1 >= 0 and y + 1 <= len(grid)-1:
                    # south west = x-1, y+1
                    # print("SW")
                    neighbour = grid[x - 1][y + 1]
                    if neighbour == 10:
                        grid[x][y] +=1
                        if grid[x][y] == 10:
                            flashCounter +=1
                if x - 1 >= 0:
                    # west = x-1, y
                    # print("W")
                    neighbour = grid[x - 1][y]
                    if neighbour == 10:
                        grid[x][y] +=1
                        if grid[x][y] == 10:
                            flashCounter +=1
                if x - 1 >= 0 and y - 1 >= 0:
                    # north west = x-1, y-1
                    # print("NW")
                    neighbour = grid[x - 1][y - 1]
                    if neighbour == 10:
                        grid[x][y] +=1
                        if grid[x][y] == 10:
                            flashCounter +=1

    print(grid)
    print(flashCounter)

    #step 3
    for i in range(row):
        for j in range(col):
            x = i
            y = j
            if grid[x][y] == 10:
                grid[x][y] = 0

    print(grid)
    print(flashCounter)

