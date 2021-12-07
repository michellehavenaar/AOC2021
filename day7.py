from collections import Counter

with open("input/i_day7.txt") as f:
    data = f.read()

data = data.split(",")
# print(data)
pos = [int(d) for d in data]
# print(pos)
highestPos = max(pos)
print(highestPos)

posCounter = Counter(pos)
# print(posCounter)
# posCounter.most_common()
sumList= []
for i in range(0, highestPos+1):
    sum = 0
    # print("target pos: " + str(i))
    for p, count in posCounter.items():
        #difference between p and targetPos
        fuel = abs(p - i)
        # print (fuel)
        #total fuel for crabs at that pos
        fuelPerPos = fuel * count
        # print(fuelPerPos)
        sum += fuelPerPos
        # print("sum: " +str(sum))
    # print("total sum: " + str(sum))
    sumList.append(sum)

# print(sumList)
print(min(sumList))

