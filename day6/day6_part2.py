from collections import Counter

with open("input/i_day6.txt") as f:
    data = f.read()

data = data.split(",")
fish = [int(d) for d in data]


#counter
startPop = Counter(fish)

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

fishPop = Fishpopulation(startCount)

Fishpopulation.createDays(fishPop,startPop)

for i in range(0,256):
    currentDay = i

    #find day
    for day in fishPop.days:
        if day["dayNumber"] == currentDay:
            #first update count
            Fishpopulation.updateCount(fishPop,day["newFish"])

            #a new fish has been born, update the days or create a new day
            addFish = day["newFish"]
            targetDay = i + 9
            dayFound = False
            for day in fishPop.days:
                if day["dayNumber"] == targetDay:
                    dayFound = True
                    day["newFish"] += addFish
            if dayFound == False:
                newDay = {
                    "dayNumber" : targetDay,
                    "newFish" : addFish
                }
                fishPop.days.append(newDay)

            #reset the fish
            targetDay = i + 7
            dayFound = False
            for day in fishPop.days:
                if day["dayNumber"] == targetDay:
                    dayFound = True
                    day["newFish"] += addFish
            if dayFound == False:
                newDay = {
                    "dayNumber" : targetDay,
                    "newFish" : addFish
                }
                fishPop.days.append(newDay)

print(fishPop.count)








