from collections import Counter

with open("day10/i_day10.txt") as f:
    text = f.read()

data = text.split("\n")

listOfLines = [list(d) for d in data]

openers = ["[", "(", "<", "{"]

closers = {
    "[" : "]",
    "(" : ")",
    "<" : ">",
    "{" : "}"
}

pointsAutoComplete = {
    ")" : 1,
    "]" : 2,
    "}" : 3,
    ">" : 4
}

pointsSyntaxErrors = {
    ")" : 3,
    "]" : 57,
    "}" : 1197,
    ">" : 25137
}

scores = []
listOfIncompleteLines = []

def checkLine(line):
    if len(line) > 0:
        for i,l in enumerate(line):
            if i < len(line) - 1:
                currentEl = l
                nextEl = line[i+1]
                if nextEl not in openers:
                    # check if the next el is a correct closer
                    correctCloser = closers[currentEl]
                    if nextEl != correctCloser:
                        #found a corrupt chunk
                        alert = f"Expected {correctCloser} but found {nextEl} in stead"
                        # print(alert)
                        #find score
                        score = pointsSyntaxErrors[nextEl]
                        scores.append(score)
                        return alert
                    else:
                        # remove the elements from the list
                        removeI = [i, i+1]
                        lineToCheck = [l for i, l in enumerate(line) if i not in removeI]
                        checkLine(lineToCheck)
                        return 
        listOfIncompleteLines.append(line)
        return
    else:
        return 

def calcAutoCompleteScore(additions):
    score = 0
    for a in additions:
        score = score * 5 
        value = pointsAutoComplete[a]
        score += value
    return score

for line in listOfLines:
    result = checkLine(line)

answerPart1 = sum(scores)
print(answerPart1)

autoCompleteScores = []
for incompleteLine in listOfIncompleteLines:
    additions = []
    for i in reversed(incompleteLine):
        addition = closers[i]
        additions.append(addition)
    autoCompleteScore = calcAutoCompleteScore(additions)
    autoCompleteScores.append(autoCompleteScore)

autoCompleteScores.sort()

answerPart2 = autoCompleteScores[len(autoCompleteScores)//2]
print(answerPart2)
    


