with open('input/practise_input.txt') as file:
    data = [int(line) for line in file]
        

def findTwo(data, sum):
    for d in data:
        remainder = sum - d
        if remainder in data:
            return (remainder * d)

print(findTwo(data,2020))

def findThree(data, sum):
    for i in data:
        remain = sum - i
        result= findTwo(data, remain)
        if result is not None:
            return (i *result )

print(findThree(data, 2020))