from collections import deque

with open("day12/i_day12.txt") as f:
    text = f.read()

data = text.split("\n")
caveMap = [line.split("-") for line in data]

class CaveSystem: 
    def __init__(self):
        self.listOfCaves = []
        self.listOfPaths = []

    def addCave(self, name, link):
        cave = Cave(name, link)
        self.listOfCaves.append(cave)

    def findAndUpdateCave(self, name, link):
        for cave in self.listOfCaves:
            if cave.name == name:
                cave.links.append(link)
                return True
        return False

    def findCaveConnections(self, name):
        for cave in self.listOfCaves:
            if cave.name == name:
                return cave.links


class Cave:
    def __init__(self, name, link):
        self.name = name
        self.links = [link]


caves = CaveSystem()
queue = deque()
path = []


def isVisitable(path, c):
    visitable = True
    if c in path and c.islower():
        visitable = False
        return visitable
    #check if the connection is a dead end
    conn = caves.findCaveConnections(c)
    if len(conn) == 1:
        if conn[0].islower():
            visitable = False
            return visitable
    return visitable


for line in caveMap:
    #try to find an allready existing cave and update it if found
    tryFindAndUpdate = caves.findAndUpdateCave(line[0], line[1])
    if tryFindAndUpdate == False:
        # create a new cave
        caves.addCave(line[0], line[1])
    #the other way around
    tryFindAndUpdate = caves.findAndUpdateCave(line[1], line[0])
    if tryFindAndUpdate == False:
        # create a new cave
        caves.addCave(line[1], line[0])

#get the start cave and begin a path and add it to the queue
path = ["start"]
queue.append(path)


# while there is something in the queue
while len(queue) != 0:
    # get the (next) path to explore from the queue
    pathToCheck = queue.popleft()
    # check the last visited cave in the path
    lastVisited = pathToCheck[-1]
    # find the last visited cave and get the connections
    connections = caves.findCaveConnections(lastVisited)
    # add each of the connections to the path and put it back into the queue if its not at an end
    for c in connections:
        #check if we can visit this connection
        if isVisitable(pathToCheck, c): 
            newPath = pathToCheck.copy()
            newPath.append(c)
            if c == "end":
                caves.listOfPaths.append(newPath)
            else:
                queue.append(newPath)

print(len(caves.listOfPaths))  


