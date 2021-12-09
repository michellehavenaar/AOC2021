with open("day9/i_day9.txt") as f:
    data = [line.replace("\n", "") for line in f]


rows = {}
for i,d in enumerate(data):
    index = i
    horizontal= [int(el) for el in d]
    rows[i] = horizontal

width = len(data[0])
height = len(rows)

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

peaks = []
# move through a row
for k, v in rows.items():
    for i in range(width):
        foundPossiblePeak = False
        foundPeak = False
        # if there is a left
        if i > 0:
            # look to the left
            lowerThenLeft = lookLeft(v[i], v[i-1])
            if lowerThenLeft == True:
                # if there is a right
                if i < width -1:
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
            possiblePeak = v[i]
            #if there is an up
            if k > 0:
                # look up
                rowUp = rows[k-1]
                valueUp = rowUp[i]
                lowerThenAbove = lookUp(v[i], valueUp)
                if lowerThenAbove == True:
                    # if there is a down
                    if k < height -1:
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
            peaks.append(v[i])

riskLevel = sum([p+1 for p in peaks])
print(riskLevel)        


                
