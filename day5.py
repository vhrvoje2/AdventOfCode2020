boardingPasses = []
with open('day5input.txt', 'r') as file:
    for item in file.readlines():
        boardingPasses.append(item.strip())

def part1():
    maxID = 0

    for boadringPass in boardingPasses:
        seatID = getSeatID(boadringPass)

        if seatID > maxID:
            maxID = seatID

    print(f"Part 1. solution {maxID}")
   
def part2():
    seatIDs = set()
    mySeatID = 0

    for boardingPass in boardingPasses:
        seatIDs.add(getSeatID(boardingPass))

    notIDs = set([seatID for seatID in range(0, 1024)])
    notIDs = notIDs - seatIDs

    for seatID in notIDs:
        if seatID not in seatIDs and seatID - 1 in seatIDs and seatID + 1 in seatIDs:
            mySeatID = seatID

    print(f"Part 2. solution {mySeatID}")

def getSeatID(boadringPass):
    row = getRow(boadringPass[:7])
    column = getColumn(boadringPass[7:])
    return row * 8 + column

def getColumn(chars):
    return calculatePos(chars, [0, 7], 4, 'L', 'R')

def getRow(chars):
    return calculatePos(chars, [0, 127], 64, 'F', 'B')

def calculatePos(chars, numRange, subtrahend, charUpper, charLower):
    for char in chars:
        if char == charUpper:
            numRange[1] -= subtrahend
        elif char == charLower:
            numRange[0] += subtrahend
        subtrahend = subtrahend // 2

    return numRange[0]

part1()
part2()
