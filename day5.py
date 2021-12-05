import re
from collections import Counter

with open("input/i_day5.txt") as f:
    data = f.readlines()

#print(data)
nums = [[int(n) for n in re.findall("\d+", line)] for line in data]
#print(nums)
print(len(nums))


#list of lines to check, only horizontal and vertical
lines = []



for x1, y1, x2, y2 in nums:
    if x1 == x2 or y1 == y2:
        lines.append([x1, y1, x2, y2])
       

#print(lines)

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
    #print(dif)
    if lineStart < lineEnd:
        step = 1
        lineEnd = lineEnd +1
    if lineStart > lineEnd:
        step = -1
        lineEnd = lineEnd -1
    coX = [x for x in range(lineStart, lineEnd, step)]
    #print(coX)
    coY = [yCo]* dif
    #print(coY)
    horLine = [list(a) for a in zip(coX, coY)]
    return horLine

#vertical
def getVerCoords(line):
    xCo = line[0]
    lineStart = line[1]
    lineEnd = line[3]
    step = 0
    dif = abs(lineStart - lineEnd) +1
    #print(dif)
    if lineStart < lineEnd:
        step = 1
        lineEnd = lineEnd +1
    if lineStart > lineEnd:
        step = -1
        lineEnd = lineEnd -1
    coY = [x for x in range(lineStart, lineEnd, step)]
    #print(coY)
    coX = [xCo]* dif
    #print(coX)
    verLine = [list(a) for a in zip(coX, coY)]
    return verLine

# for every line make all the coordinates
listOfCoords = []
for line in lines:
    #print(line)
    if line[0] == line[2]:
        #print("vertical line")
        #print(line)
        vCo = getVerCoords(line)
        #print(vCo)
        for co in vCo:
            c = Coord(co[0],co[1])
            
            listOfCoords.append(c.co)
    if line[1] == line[3]:
        #print("horizontal line")
        #print(line)
        hCo = getHorCoords(line)
        #print(hCo)
        for co in hCo:
            c = Coord(co[0],co[1])
            listOfCoords.append(c.co)


#print(listOfCoords)
dups = [ele for ele, count in Counter(listOfCoords).items() if count >1]
print(len(dups))


