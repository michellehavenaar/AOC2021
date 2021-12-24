from collections import Counter

with open("day14/i_day14.txt") as f:
    text = f.read()

data = text.split("\n\n")

template = data[0]
template = [t for t in template]

listOfPairs = [template[i] + template[i+1] for i in range(len(template)-1)]

rules = data[1]
rules = rules.split("\n")
rules = [r.split("->") for r in rules]
rules = {r[0].strip(): r[1].strip() for r in rules}


# make the initial count with the starting template
templateCount = Counter(template)
countElements = {k: v for k, v in templateCount.items()}

countPairs = {}

for pair in listOfPairs:
    if pair in countPairs:
        countPairs[pair] +=1
    else:
        countPairs[pair] = 1

step = 0
while step < 40:
    # make a temporary pair counter to count all the new pairs of this step
    # at the end of the step write the temp over the original 
    # so you can start every step with the pairs from the last step only
    newCountPairs = {}
    for k, v in list(countPairs.items()):
        pair = k
        count = v
        # find the pair in the rules
        insert = rules[pair]
        # and add the insert to the element count, with the count being the amount of times that the parent pair appeared
        if insert in countElements:
            countElements[insert] += count
        else: 
            countElements[insert] = count
        
        # make the new pairs
        left = pair[0]+insert
        right = insert + pair[1]
        pairs = [left, right]
        # and add them to a new pair counter, with the count being the amount of times that parent pair appeared
        for p in pairs:
            if p in newCountPairs:
                newCountPairs[p] += count
            else:
                newCountPairs[p] = count
    step +=1
    countPairs = newCountPairs


maxValue = countElements[max(countElements, key = countElements.get)]
minValue = countElements[min(countElements, key = countElements.get)]

answer = maxValue - minValue
print(answer)
