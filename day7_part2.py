# test = range(0,1968)
# sumList =sum(test)
# print(sumList)

from collections import Counter

with open("input/i_day7.txt") as f:
    data = f.read()

data = data.split(",")
# print(data)
pos = [int(d) for d in data]
# print(pos)
highestPos = max(pos)
# print(highestPos)

posCounter = Counter(pos)
# print(posCounter)

#calculate the sum of a range like, if there are 5 steps (1+2+3+4+5)
#hit limit :( so no recursion
# def calcSum(n):
#     if n < 1:
#         return n
#     return n + calcSum(n-1)

#print(calcSum(4))


# sumList= []
# for i in range(0, highestPos+1):
#     sum = 0
#     # print("target pos: " + str(i))
#     for p, count in posCounter.items():
#         #difference between p and targetPos
#         steps = abs(p - i)
#         # print(steps)
#         fuelPerCrab = calcSum(steps)
#         # print(fuelPerCrab)
#         fuelPerPos = fuelPerCrab * count
#         sum += fuelPerPos
#     sumList.append(sum)

# print(min(sumList))

sumList= []
for i in range(0, highestPos+1):
    total = 0
    # print("target pos: " + str(i))
    for p, count in posCounter.items():
        #difference between p and targetPos
        steps = abs(p - i)
        # print(steps)
        fuelList = list(range(1,steps+1))
        # print(fuelList)
        fuelPerCrab = sum(fuelList)
        fuelPerPos = fuelPerCrab * count
        total += fuelPerPos
    sumList.append(total)

print(min(sumList))

