with open('input/i_day3.txt') as file:
    data = [line.replace("\n", "") for line in file]

#testdata = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]


def gamma(data):
    gammaRate = "" 
    for i in range(12):
        bits = [int(d[i]) for d in data]
        zeros = bits.count(0)
        ones = bits.count(1)
        if zeros > ones:
            gammaRate += "0"
        if ones > zeros:
            gammaRate += "1"
    return gammaRate
    
def epsilon(data):
    epsilonRate = "" 
    for i in range(12):
        bits = [int(d[i]) for d in data]
        zeros = bits.count(0)
        ones = bits.count(1)
        if zeros < ones:
            epsilonRate += "0"
        if ones < zeros:
            epsilonRate += "1"
    return epsilonRate

gammaRateDec = (int(gamma(data), 2))
epsilonRateDec = (int(epsilon(data), 2))

print(gammaRateDec * epsilonRateDec)


def oxygen(data):
    for i in range(12):
        bits = [int(d[i]) for d in data]
        zeros = bits.count(0)
        ones = bits.count(1)
        if zeros > ones:
            number = 0
        if zeros <= ones:
            number = 1
        data = [d for d in data if int(d[i]) == number]
        if len(data) == 1:
            break
    return (data[0])

def co2(data):
    for i in range(12):
        bits = [int(d[i]) for d in data]
        zeros = bits.count(0)
        ones = bits.count(1)
        if zeros <= ones:
            number = 0
        if zeros > ones:
            number = 1
        data = [d for d in data if int(d[i]) == number]
        if len(data) == 1:
            break
    return (data[0])

oxygenRateDec = (int(oxygen(data), 2))
co2RateDec = (int(co2(data), 2))

print(oxygenRateDec * co2RateDec)
