with open("input/i_day6.txt") as f:
    data = f.read()

data = data.split(",")
fish = [int(d) for d in data]

def fishProducer(fish):
    for i, f in enumerate(fish):
        if f > 0:
            fish[i] = f -1
        if f == 0:
            fish[i] = 6
            fish.append(9)
    return fish


for i in range(80):
    fishProducer(fish)

print(len(fish))



