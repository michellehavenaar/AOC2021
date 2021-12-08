from collections import Counter

with open("input/i_day8test.txt") as f:
    data = f.readlines()

data = [d.replace("\n", "") for d in data]
data = [d.split("|") for d in data]
print(data)

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

segments are numbered 1-7
digit 0 consists of segments 1,3,6,7,5,2
digit 1 consists of segments 3,6
digit 2 consists of segments 1,3,4,5,7
digit 3 consists of segments 1,3,4,6,7
digit 4 consists of segments 2,4,3,6
digit 5 consists of segments 1,2,4,6,7
digit 6 consists of segments 1,2,5,4,6,7
digit 7 consists of segments 1,3,6
digit 8 consists of segments 1,2,3,4,5,6,7
digit 9 consists of segments 1,2,3,4,6,7
"""
listsOfDigits = [[1,3,6,7,5,2], [3,6], [1,3,4,5,7], [1,3,4,6,7], [2,4,3,6], [1,2,4,6,7],[1,2,5,4,6,7],[1,3,6],[1,2,3,4,5,6,7],[1,2,3,4,6,7]]
flat = [item for digit in listsOfDigits for item in digit]
print(flat)
segmentCounter = Counter(flat)
print(segmentCounter)

# class TranslationTable:
#     def __init__(self, number):
#         self.a = number
#         self.b = number
#         self.c = number
#         self.d = number
#         self.e = number
#         self.f = number
#         self.g = number

#     def updateTable(self,letter,number):
#         self.letter = number


# test = TranslationTable(0)
# letter = "b"
# number = 3
# test.updateTable(test, letter, number)
# print(test.b)

# translationTable = {}
# translationTable["a"] = 3
# print(translationTable)


for input, output in data:
    inputList = [i for i in input.split(" ") if i]
    inputCounter = Counter(input.replace(" ", ""))
    outputList = [o for o in output.split(" ") if o]
    print(inputList)
    print(inputCounter)
    # print(outputList)
    translationTable = {}
    #start with digit 2
    # should be segment 3 and 6
    digit2 = [i for i in inputList if len(i) == 2]
    digit2 = digit2[0]
    print(digit2)
    for letter in digit2:
        if inputCounter[letter] == segmentCounter[3]:
            translationTable[3] = letter
        else:
            translationTable[6] = letter
    print(translationTable)

    # now digit 7
    # should be segment 1, 3 and 6
    # we allready know segment 3 and 6
    digit7 = [i for i in inputList if len(i) == 3]
    digit7 = digit7[0]
    print(digit7)
    #check the letter that is not segment 3 or 6
    



            


            



