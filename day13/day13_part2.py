with open("day13/i_day13.txt") as f:
    text = f.read()

data = text.split("\n\n")

instructions = data[-1]
instructions = instructions.split("\n")

listOfInstructions = []
for i in instructions:
    instr = i.replace("fold along ", "")
    instruction = instr.split("=")
    axis = str(instruction[0])
    value = int(instruction[1])
    instruction = [axis, value]
    listOfInstructions.append(instruction)

coords = data[0]
coords = coords.split("\n")
coords = [c.split(",") for c in coords]

listOfCoords = []
for c in coords:
    co = [int(el) for el in c]
    listOfCoords.append(co)


def mirror(coord, fold, axis):
    co = coord[axis]
    dif = co - fold
    newco = fold - dif
    coord[axis] = newco


def fold(axis, value):
    if axis == "y":
        ax = 1
    if axis == "x":
        ax = 0
    for co in listOfCoords:
        if co[ax] > value:
            mirror(co, value, ax)


for instruction in listOfInstructions:
    
    fold(instruction[0], instruction[1])
    #remove duplicates
    seen = []
    for co in listOfCoords:
        if co not in seen:
            seen.append(co)
    listOfCoords = seen

#sort by x values to get the width of the grid
sortedListX = sorted(listOfCoords, key = lambda k: [k[0],k[1]])
# max width is the x coordinate of the last element
maxWidth = sortedListX[-1][0] +1

#sort by y values to get the length of the grid
sortedListY = sorted(listOfCoords, key = lambda k: [k[1],k[0]])
# max length is the y coordinate of the last element
maxLength = sortedListY[-1][1] +1

# make a grid
grid = [ ["."] * maxWidth for _ in range(maxLength)]

for co in listOfCoords:
    x = co[0]
    y = co[1]
    grid[y][x] = "#"

for row in grid:
    print(row)
