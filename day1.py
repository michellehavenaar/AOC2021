with open('input/i_day1.txt') as file:
    data = [int(line) for line in file]

#test = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

def depthCounter(data):
    sub = 0
    count = 0
    for d in data:
        if d > sub:
            count += 1
        sub = d
    
    return count-1

print(depthCounter(data))


def depthCounterAdvanced(data):
    l = len(data)
    prevSum = 0
    count = 0 
    for index, item in enumerate(data):
        if index < (l -2):
            sum = data[index] + data[index +1] + data[index+2]
            if sum > prevSum:
                count +=1
            prevSum = sum

    return count-1

print(depthCounterAdvanced(data))