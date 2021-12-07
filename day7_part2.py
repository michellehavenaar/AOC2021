from collections import Counter

with open("input/i_day7.txt") as f:
    data = f.read()

data = data.split(",")
pos = [int(d) for d in data]
highestPos = max(pos)

posCounter = Counter(pos)

def fuelCostToTarget(target, position, count):
    steps = abs(position - target)
    fuelList = list(range(1, steps+1))
    fuelPerCrab = sum(fuelList)
    fuelPerPos = fuelPerCrab * count
    return fuelPerPos

sumList= []
for i in range(0, highestPos+1):
    total = 0
    for p, count in posCounter.items():
        totalFuelperPos = fuelCostToTarget(i, p, count)
        total += totalFuelperPos
    sumList.append(total)

print(sumList)
print(min(sumList))
