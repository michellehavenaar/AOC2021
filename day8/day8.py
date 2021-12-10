with open("input/i_day8.txt") as f:
    data = f.readlines()

data = [d.replace("\n", "") for d in data]
data = [d.split("|") for d in data]

"""
0 : 6 segments
1 : 2 segments
2 : 5 segments
3 : 5 segments
4 : 4 segments
5 : 5 segments
6 : 6 segments
7 : 3 segments
8 : 7 segments
9 : 6 segments
"""
sum = 0
for input, output in data:
    outputList = [o for o in output.split(" ") if o]
    outputListFiltered = [o for o in outputList if len(o) == 2 or len(o) == 3 or len(o) == 4 or len(o) == 7]
    sum += len(outputListFiltered)

print(sum)
