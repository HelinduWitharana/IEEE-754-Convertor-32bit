def printFormatBit(inSign, inExponent, inMantissa):
    bitPrint = '|'
    for x in range(32):
        if (x == 0):
            bitPrint += inSign + '| |'
        elif (x > 0 and x < 9):
            bitPrint += inExponent[x-1] + '|'
            if (x == 8):
                bitPrint += ' |'
        elif (x >= 9):
            bitPrint += inMantissa[x-9] + '|'
    print(' _  ' + ' _'*8 + '  ' + ' _'*23)
    print(bitPrint)


def addZeros(inVal, PM, count):
    out = ''
    if (PM == 'P'):
        out = inVal
        for i in range(count-len(inVal)):
            out += '0'
    elif (PM == 'M'):
        for i in range(count-len(inVal)):
            out += '0'
        out += inVal
    return out


def run(inVal):
    if (inVal < 0):
        finalSign = '1'
        inVal *= -1
    else:
        finalSign = '0'

    # print(inVal)

    fPoint = 0
    n1Point = 0

    while(not(str(inVal)[fPoint] == ".")):
        fPoint += 1
    # print("'.' is at: ", fPoint)

    while(not(str(inVal)[n1Point] == "1")):
        n1Point += 1
    # print("'1' is at: ", n1Point)

    val = fPoint - n1Point

    # print('')

    if(val < 0):
        initExponent = (fPoint - n1Point)
        initMantissa = (inVal/(10**(fPoint - n1Point)))

        print(str(initMantissa)+'x2^'+str(initExponent))

        finalExponent = str(bin(127+initExponent))[2:]
        finalMantissa = str(initMantissa)[2:]

        printFormatBit(finalSign, addZeros(finalExponent, 'M', 8),
                       addZeros(finalMantissa, 'P', 23))

    else:
        initExponent = ((fPoint - n1Point) - 1)
        initMantissa = (inVal/(10**((fPoint - n1Point) - 1)))

        print(str(initMantissa)+'x2^'+str(initExponent))

        finalExponent = str(bin(127+initExponent))[2:]
        finalMantissa = str(initMantissa)[2:]

        printFormatBit(finalSign, addZeros(finalExponent, 'M', 8),
                       addZeros(finalMantissa, 'P', 23))


run(float(input("Enter binary number: ")))