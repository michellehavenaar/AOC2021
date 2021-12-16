from collections import deque

with open("day11/i_day11.txt") as f:
    text = f.read()

data = text.split("\n")
data = [list(d) for d in data]
# print(data)

grid = []
for d in data:
    row = [int(el) for el in d]
    grid.append(row)
print(grid)

row = len(grid[0])
col = len(grid)

queue = deque()
flashCounter = 0

def flash(i,j):
    # print(f"flashing for: {i}, {j}")
    if i - 1 >= 0:
        # print("N")
        neighbour = grid[i-1][j]
        if neighbour <= 9:
            grid[i-1][j] +=1
            #if neighbour is now 10 then add it to the queue to look at later
            if grid[i-1][j] == 10:
                octo = [i-1,j]
                queue.append(octo)
    if i - 1 >= 0 and j + 1 < len(grid[0]):
        # print("NE")
        neighbour = grid[i-1][j+1]
        if neighbour <= 9:
            grid[i-1][j+1] +=1
            if grid[i-1][j+1] == 10:
                octo = [i-1,j+1]
                queue.append(octo)
    if j + 1 < len(grid[0]):
        # print("E")
        neighbour = grid[i][j+1]
        if neighbour <= 9:
            grid[i][j+1] +=1
            if grid[i][j+1] == 10:
                octo = [i, j+1]
                queue.append(octo)
    if i + 1 < len(grid) and j + 1 < len(grid[0]):
        # print("SE")
        neighbour = grid[i + 1][j + 1]
        if neighbour <= 9:
            grid[i + 1][j + 1] +=1
            if grid[i + 1][j + 1] == 10:
                octo = [i + 1, j + 1]
                queue.append(octo)
    if i + 1 < len(grid):
        # print("S")
        neighbour = grid[i+1][j]
        if neighbour <= 9:
            grid[i+1][j] +=1
            if grid[i+1][j] == 10:
                octo = [i+1, j]
                queue.append(octo)
    if i + 1 < len(grid) and j - 1 >= 0:
        # print("SW")
        neighbour = grid[i + 1][j -1]
        if neighbour <= 9:
            grid[i + 1][j -1] +=1
            if grid[i + 1][j -1] == 10:
                octo = [i + 1, j -1]
                queue.append(octo)
    if j - 1 >= 0:
        # print("W")
        neighbour = grid[i][j - 1]
        if neighbour <= 9:
            grid[i][j - 1] +=1
            if grid[i][j - 1] == 10:
                octo = [i, j - 1]
                queue.append(octo)
    if i - 1 >= 0 and j - 1 >= 0:
        # print("NW")
        neighbour = grid[i - 1][j - 1]
        if neighbour <= 9:
            grid[i - 1][j - 1] +=1
            if grid[i - 1][j - 1] == 10:
                octo = [i - 1, j - 1]
                queue.append(octo)


testGrid = [el for row in grid for el in row if el != 0]
step = 0
while len(testGrid) != 0:
    step +=1
    #step 1
    for i,row in enumerate(grid):
        for j,el in enumerate(row):
            grid[i][j] +=1

    #step 2
    for i,row in enumerate(grid):
        for j,el in enumerate(row):
            #if 10 then add them to the queue
            if grid[i][j] == 10:
                octo = [i, j]
                queue.append(octo)
    # take the first from the queue and flash the neighbours
    while len(queue) != 0:
        flashingOcto = queue.popleft()
        flashCounter += 1
        flash(flashingOcto[0],flashingOcto[1])
    
    #step 3
    for i,row in enumerate(grid):
        for j,el in enumerate(row):
            if grid[i][j] == 10:
                grid[i][j]  = 0
    
    testGrid = [el for row in grid for el in row if el != 0]


print(grid)
print(flashCounter)
print(step)

