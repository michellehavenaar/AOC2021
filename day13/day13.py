with open("day13/i_day13test.txt") as f:
    text = f.read()

# print(text)

data = text.split("\n\n")
# print(data)

instructions = data[-1]
instructions = instructions.split("\n")
# print(instructions)

coords = data[0]
coords = coords.split("\n")
coords = [c.split(",") for c in coords]
# print(coords)

unsortedListOfCoords = []
for c in coords:
    co = [int(el) for el in c]
    unsortedListOfCoords.append(co)

# print(unsortedListOfCoords)

def mergeSort(list):
    n = len(list)
    if n == 1: 
        return
    else:
        mid = n //2
        left = list[: mid]
        print(left)
        right = list[mid :]
        print(right)

        mergeSort(left)
        mergeSort(right)


mergeSort(unsortedListOfCoords)


