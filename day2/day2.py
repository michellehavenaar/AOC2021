with open('input/i_day2.txt') as file:
    rawData = [line.replace("\n", "") for line in file]
    data = [d.split(" ") for d in rawData]

#test
#testData = [["forward", "5"], ["down", "5"], ["forward", "8"], ["up", "3"], ["down","8"], ["forward", "2"]]


def calcPos(data):
    hPos = 0
    depth = 0

    for command in data:
        dir = command[0]
        unit = int(command[1])
        if dir == "forward":
            hPos += unit
        elif dir == "down":
            depth += unit
        elif dir == "up":
            depth -= unit

    return (hPos,depth)

result = calcPos(data)

answer = result[0] * result[1]
print(answer)

def calcPos2(data):
    hPos = 0
    aim = 0
    depth = 0

    for command in data:
        dir = command[0]
        unit = int(command[1])
        if dir == "forward":
            hPos += unit
            depth += (aim * unit)
        elif dir == "down":
            aim += unit
        elif dir == "up":
            aim -= unit

    return (hPos,depth)

result = calcPos2(data)

answer = result[0] * result[1]
print(answer)