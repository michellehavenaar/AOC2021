from collections import Counter

with open("input/i_day7.txt") as f:
    data = f.read()

data = data.split(",")
pos = [int(d) for d in data]
highestPos = max(pos)

posCounter = Counter(pos)
sumList= []
for i in range(0, highestPos+1):
    sum = 0
    for p, count in posCounter.items():
        fuel = abs(p - i)
        fuelPerPos = fuel * count
        sum += fuelPerPos
    sumList.append(sum)

print(min(sumList))

