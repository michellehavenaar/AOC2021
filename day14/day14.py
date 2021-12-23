with open("day14/i_day14test.txt") as f:
    text = f.read()

data = text.split("\n\n")
print(data)

template = data[0]
template = [t for t in template]

# listOfPairs = []

# for i in range(len(template)-1):
#     pair = template[i] + template[i+1]
#     listOfPairs.append(pair)

# print(listOfPairs)

listOfPairs = [template[i] + template[i+1] for i in range(len(template)-1)]

print(listOfPairs)