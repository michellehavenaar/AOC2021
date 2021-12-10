from collections import deque
import numpy

with open("day9/i_day9.txt") as f:
    data = [line.replace("\n", "") for line in f]

rows = {}
for i,d in enumerate(data):
    index = i
    heights= [int(el) for el in d]
    rows[i] = heights

horLenght = len(data[0])
verLenght = len(rows)

def lookLeft(value, leftValue):
    if value < leftValue:
        return True
    else:
        return False

def lookRight(value, rightValue):
    if value < rightValue:
        return True
    else:
        return False

def lookUp(value, upValue):
    if value < upValue:
        return True
    else:
        return False

def lookDown(value, downValue):
    if value < downValue:
        return True
    else:
        return False

def findPeak(k, v, i):
    foundPossiblePeak = False
    foundPeak = False
    # if there is a left
    if i > 0:
        # look to the left
        lowerThenLeft = lookLeft(v[i], v[i-1])
        if lowerThenLeft == True:
            # if there is a right
            if i < horLenght -1:
                # look to the right
                lowerThenRight = lookRight(v[i], v[i+1])
                if lowerThenRight == True:
                    foundPossiblePeak = True
            else:
                # there is no right
                foundPossiblePeak = True
    else:
        # look to the right
        lowerThenRight = lookRight(v[i], v[i+1])
        if lowerThenRight == True:
            foundPossiblePeak = True
    if foundPossiblePeak == True:
        #if there is an up
        if k > 0:
            # look up
            rowUp = rows[k-1]
            valueUp = rowUp[i]
            lowerThenAbove = lookUp(v[i], valueUp)
            if lowerThenAbove == True:
                # if there is a down
                if k < verLenght -1:
                    # look down
                    rowDown = rows[k+1]
                    valueDown = rowDown[i]
                    lowerThenDown = lookDown(v[i], valueDown)
                    if lowerThenDown == True:
                        foundPeak = True
                else:
                    # last row
                    foundPeak = True
        else:
            # look down
            rowDown = rows[k+1]
            valueDown = rowDown[i]
            lowerThenDown = lookDown(v[i], valueDown)
            if lowerThenDown == True:
                foundPeak = True
    if foundPeak == True:
        return True
    else:
        return False

class Node:
    def __init__(self, value, row, key, index):
        self.value = value
        self.row = row
        self.key = key
        self.index = index
        self.co = (key,index)


def lookAround(node):
    currentRow = node.row
    currentIndex = node.index
    currentKey = node.key
    # if there is a left 
    if currentIndex > 0:
        #look to left of the node and if there is not a 9 create that position into a new Node and add it to the queue
        leftValue = currentRow[currentIndex -1]
        if leftValue != 9:
            #create new node
            node = Node(leftValue, currentRow, currentKey, currentIndex -1)
            preventDupNodes = [n for n in listOfNodes if n.co == node.co]
            if len(preventDupNodes) == 0:
                queue.append(node)
                listOfNodes.append(node)
    # if there is a right
    if currentIndex < horLenght -1:
        rightValue = currentRow[currentIndex +1]
        if rightValue != 9:
            node = Node(rightValue, currentRow, currentKey, currentIndex +1)
            preventDupNodes = [n for n in listOfNodes if n.co == node.co]
            if len(preventDupNodes) == 0:
                queue.append(node)
                listOfNodes.append(node)
    # if there is an up
    if currentKey> 0:
        rowUp = rows[currentKey -1]
        valueUp = rowUp[currentIndex]
        if valueUp != 9:
            node = Node(valueUp, rowUp, currentKey-1, currentIndex)
            preventDupNodes = [n for n in listOfNodes if n.co == node.co]
            if len(preventDupNodes) == 0:
                queue.append(node)
                listOfNodes.append(node)
    # if there is a down
    if currentKey < verLenght -1:
        rowDown = rows[currentKey +1]
        valueDown = rowDown[currentIndex]
        if valueDown != 9:
            node = Node(valueDown, rowDown, currentKey +1, currentIndex)
            preventDupNodes = [n for n in listOfNodes if n.co == node.co]
            if len(preventDupNodes) == 0:
                queue.append(node)
                listOfNodes.append(node)

listOfBasinLengths = []
# move through a row and find a peak (which is actually a bottom but that sounds weird)
for k, v in rows.items():
    for i in range(horLenght):
        peak = findPeak(k, v, i)
        if peak == True:
            listOfNodes = []
            queue = deque()
            basin = []
            #make a node for the peak
            value = v[i]
            row = v
            key = k
            index = i
            peakNode = Node(value, row, key, index)
            listOfNodes.append(peakNode)
            lookAround(peakNode)
            # done looking around
            # add value to the basin
            basin.append(peakNode.value)
            
            # while there is something in the queue
            while len(queue) != 0:
                # get the first node from the queue
                nextNode = queue.popleft()
                lookAround(nextNode)
                basin.append(nextNode.value)
            basinLength = len(basin)
            listOfBasinLengths.append(basinLength)

listOfBasinLengths.sort()
biggestBasins = listOfBasinLengths[-3:]
result = numpy.prod(biggestBasins)
print(result)

            

            

