with open("day13/i_day13test.txt") as f:
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


firstInst = listOfInstructions[0]
fold(firstInst[0], firstInst[1])

#remove duplicates
seen = []
for co in listOfCoords:
    if co not in seen:
        seen.append(co)

print(len(seen))



