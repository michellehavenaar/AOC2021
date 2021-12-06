from collections import Counter

with open("input/i_day6test.txt") as f:
    data = f.read()

data = data.split(",")
fish = [int(d) for d in data]

print(fish)

#counter
startPop = Counter(fish)
print(startPop)

# for s, count in startPop.items():
#     print(s, count)

class Fishpopulation:
    def __init__(self, count):
        self.count = count
    
    def createDays(self, startPop):
        self.days = []

        for s, count in startPop.items():
            day = {
                "dayNumber" : s,
                "newFish" : count
            }
            self.days.append(day)

    def updateCount(self, newFish):
        self.count += newFish
            

startCount = sum(startPop.values())
print(startCount)

fishPop = Fishpopulation(startCount)

print(fishPop.count)

Fishpopulation.createDays(fishPop,startPop)
print(fishPop.days)

# for day in fishPop.days:
#     print(day["dayNumber"])

#start at day 0
#find the day this tells you how many fishes are being added that day





# dayFound = findDayByNumber(1, fishPop.days)
# if len(dayFound) == 0:
#     print("do nothing")
# if len(dayFound) > 0:
#     print(dayFound)
#     print(dayFound)
# #     Fishpopulation.updateCount(fishPop, dayFound["newFish"])

# print(fishPop.count)
# number = 0
# next(day for day in fishPop.days if day["dayNumber"] == number)
# Fishpopulation.updateCount(fishPop,2)
# print(fishPop.count)





