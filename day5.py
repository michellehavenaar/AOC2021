import re
from collections import Counter

with open("input/i_day5.txt") as f:
    data = f.readlines()



nums = [[int(n) for n in re.findall("\d+", line)] for line in data]

#list of lines to check
lines = []

#part 1, only vertical and horizontal lines, comment this out if you want part 2
# for x1, y1, x2, y2 in nums:
#     if x1 == x2 or y1 == y2:
#         lines.append([x1, y1, x2, y2])

#part 2, all lines, comment this out if you want part 1
for x1, y1, x2, y2 in nums:
    lines.append([x1, y1, x2, y2])
  
       
class Coord:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.co = (x,y)

#horizontal
def getHorCoords(line):
    yCo = line[1]
    lineStart = line[0]
    lineEnd = line[2]
    step = 0
    dif = abs(lineStart - lineEnd) +1
    if lineStart < lineEnd:
        step = 1
        lineEnd = lineEnd +1
    if lineStart > lineEnd:
        step = -1
        lineEnd = lineEnd -1
    xCoords = [x for x in range(lineStart, lineEnd, step)]
    yCoords= [yCo]* dif
    horLine = [list(a) for a in zip(xCoords, yCoords)]
    return horLine

#vertical
def getVerCoords(line):
    xCo = line[0]
    lineStart = line[1]
    lineEnd = line[3]
    step = 0
    dif = abs(lineStart - lineEnd) +1
    if lineStart < lineEnd:
        step = 1
        lineEnd = lineEnd +1
    if lineStart > lineEnd:
        step = -1
        lineEnd = lineEnd -1
    yCoords = [y for y in range(lineStart, lineEnd, step)]
    xCoords = [xCo]* dif
    verLine = [list(a) for a in zip(xCoords, yCoords)]
    return verLine

#diagonal
def getDiagCoords(line):
    startX = line[0]
    endX = line[2]
    startY = line[1]
    endY = line[3]
    if startX > endX:
        endX = endX -1
        step = -1
        xCoords = [x for x in range(startX, endX, step)]
    if startX < endX:
        endX = endX +1
        step = +1
        xCoords = [x for x in range(startX, endX, step)]
    if startY > endY:
        endY = endY -1
        step = -1
        yCoords = [y for y in range(startY, endY, step)]
    if startY < endY:
        endY = endY +1
        step = +1
        yCoords = [y for y in range(startY, endY, step)]
    diagLine = [list(a) for a in zip(xCoords, yCoords)]
    return diagLine

# for every line make all the coordinates
listOfCoords = []
for line in lines:
    if line[0] == line[2]:
        # this is a vertical line
        vCo = getVerCoords(line)
        for co in vCo:
            c = Coord(co[0],co[1])
            listOfCoords.append(c.co)
    elif line[1] == line[3]:
        # this is a horizontal line
        hCo = getHorCoords(line)
        for co in hCo:
            c = Coord(co[0],co[1])
            listOfCoords.append(c.co)
    else:
        #this is a diagonal line
        dCo = getDiagCoords(line)
        for co in dCo:
            c = Coord(co[0],co[1])
            listOfCoords.append(c.co)

dups = [ele for ele, count in Counter(listOfCoords).items() if count >1]
print(len(dups))
