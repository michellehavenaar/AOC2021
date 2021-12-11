with open("day11/i_day11test.txt") as f:
    text = f.read()

data = text.split("\n")
data = [list(d) for d in data]

grid = []
for d in data:
    row = [int(el) for el in d]
    grid.append(row)
print(grid)

row = len(grid)
col = len(grid[0])

def incFromNeighbours(x,y):
    # north = x, y-1
    # north east = x+1, y-1
    # east = x+1, y
    # south east = x+1, y+1
    # south = x, y+1
    # south west = x-1, y+1
    # west = x-1, y
    # nort west = x-1, y-1
    pass

for i in range(row):
    for j in range(col):
        x = i
        y = j
        value = grid[x][y]
        grid[x][y] = value +1

print(grid)

