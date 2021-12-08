from collections import Counter

with open("input/i_day8.txt") as f:
    data = f.readlines()

data = [d.replace("\n", "") for d in data]
data = [d.split("|") for d in data]


d0 = [1, 2, 3, 5, 6, 7]
d1 = [3, 6]
d2 = [1, 3, 4, 5, 7]
d3 = [1, 3, 4, 6, 7]
d4 = [2, 3, 4, 6]
d5 = [1, 2, 4, 6, 7]
d6 = [1, 2, 4, 5, 6, 7]
d7 = [1, 3, 6]
d8 = [1, 2, 3, 4, 5, 6, 7]
d9 = [1, 2, 3, 4, 6, 7]


listOfDictDigits = [{0:d0}, {1:d1}, {2:d2}, {3:d3}, {4:d4}, {5:d5}, {6:d6}, {7:d7}, {8:d8}, {9:d9}]

listsOfDigits = [[1, 2, 3, 5, 6, 7], [3, 6], [1, 3, 4, 5, 7], [1, 3, 4, 6, 7], [2, 3, 4, 6], [1, 2, 4, 6, 7],[1, 2, 4, 5, 6, 7],[1, 3, 6],[1, 2, 3, 4, 5, 6, 7],[1, 2, 3, 4, 6, 7]]
flat = [item for digit in listsOfDigits for item in digit]
# occurences of every segment
segmentCounter = Counter(flat)

listOfNumbers = []
for input, output in data:
    inputList = [i for i in input.split(" ") if i]
    inputCounter = Counter(input.replace(" ", ""))
    outputList = [o for o in output.split(" ") if o]
    translationTable = {}

    # start with digit 1
    # should be segment 3 and 6
    digit1 = [i for i in inputList if len(i) == 2]
    digit1 = digit1[0]
    for letter in digit1:
        #check if the letter has the same amount of occurences as the occurences of the segment
        if inputCounter[letter] == segmentCounter[3]:
            translationTable[3] = letter
        else:
            translationTable[6] = letter

    # now digit 7
    # should be segment 1, 3 and 6
    # we allready know segment 3 and 6
    digit7 = [i for i in inputList if len(i) == 3]
    digit7 = digit7[0]
    # find the letter that is not segment 3 and not segment 6
    # this letter is then segment 1
    letter = [l for l in digit7 if l != translationTable[3] and l != translationTable[6]]
    translationTable[1]=letter[0]

    # now digit 4
    # should be segment 2,3,4,6
    # we allready know segment 3 and 6
    digit4 = [i for i in inputList if len(i) == 4]
    digit4 = digit4[0]
    #check the letter that is not segment 3 or 6
    letter = [l for l in digit4 if l != translationTable[3] and l != translationTable[6]]
    for l in letter:
        #check if the letter has the same amount of occurences as the occurences of the segment
        if inputCounter[l] == segmentCounter[2]:
            translationTable[2] = l
        else:
            translationTable[4] = l

    #now digit 8
    # should be segment 1,2,3,4,5,6,7,8
    # we allready know 1,2,3,4,6
    digit8 = [i for i in inputList if len(i) == 7]
    digit8 = digit8[0]
    # check the letter that is not segment 1,2,3,4,6
    translationValues = translationTable.values()
    letter = [l for l in digit8 if l not in translationValues]
    for l in letter:
        #check if the letter has the same amount of occurences as the occurences of the segment
        if inputCounter[l] == segmentCounter[5]:
            translationTable[5] = l
        else:
            translationTable[7] = l

    # now the translation table is complete
    # translate the output
    number = ""
    for o in outputList:
        segment = []
        for letter in o:
            #find letter in translationtable
            for num, let in translationTable.items():
                if let == letter:
                    segment.append(num)
        segment.sort()
        # find the digit that belongs to the segment combination
        for dict in listOfDictDigits:
            for d, seg in dict.items():
                if seg == segment:
                    # and build the number
                    number += str(d)
    
    # add the number to the list of numbers as an int
    listOfNumbers.append(int(number))

# get the sum of the list
print(sum(listOfNumbers))

        



    
   
    



            


            



