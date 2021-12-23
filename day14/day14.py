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
count = {k: v for k, v in templateCount.items()}


def polymer(pair, step):
    # count the steps in the tree and stop at 10
    if step == 10:
        return
    else:
        # for each pair we check, we get the inserted value and add that to the count
        insert = rules[pair]
        if insert in count:
            count[insert] += 1
        else:
            count[insert] = 1

        # that is one layer of the tree counted, we update the step
        step +=1

        # now we make new pairs with the inserted value
        left = pair[0]+insert
        right = insert + pair[1]

        # and then do everything again for each new pair and so on
        polymer(left, step)
        polymer(right, step)

for pair in listOfPairs:
    step = 0
    polymer(pair, step)

print(count)

maxValue = count[max(count, key = count.get)]
minValue = count[min(count, key = count.get)]

answer = maxValue - minValue
print(answer)