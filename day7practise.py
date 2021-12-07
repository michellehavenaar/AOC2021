from collections import Counter

with open("input/i_day7.txt") as f:
    data = f.read()

data = data.split(",")
pos = [int(d) for d in data]

pos.sort()

highestPos = max(pos)
middle = highestPos/2
middle = int(middle)


def fuelCostToTarget(target, position, count):
    steps = abs(position - target)
    fuelList = list(range(1, steps+1))
    fuelPerCrab = sum(fuelList)
    fuelPerPos = fuelPerCrab * count
    return fuelPerPos


posCounter = Counter(pos)

def totalFueltoTarget(target, listOfPositions):
    total = 0
    for p, count in listOfPositions.items():
        totalFuelperPos = fuelCostToTarget(target, p, count)
        total += totalFuelperPos
    return total


def searchMinFuel(pointer, listOfPos):
    # get total fuel cost to target start with target middle
    cost = totalFueltoTarget(pointer, listOfPos)
    # print(cost)
    # try the position to the left of the pointer
    leftCost = totalFueltoTarget(pointer-1, listOfPos)
    # print(leftCost)
    if leftCost > cost:
        #try the position to the right of the pointer
        rightCost = totalFueltoTarget(pointer+1, listOfPos)
        # print(rightCost)
        if rightCost > cost:
            #the cost is lower then left and right so you found the bottom
            print(cost)
            return cost
        else:
            #move the pointer to the right
            searchMinFuel(pointer+1, listOfPos)
    else:
        #move the pointer to the left
        searchMinFuel(pointer-1, listOfPos)


result = searchMinFuel(middle, posCounter)
print(result)