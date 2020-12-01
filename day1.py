values = []
with open('day1input.txt', 'r') as file:
    for item in file.readlines():
        values.append(int(item.strip()))

def part1(values):
    valuesSet = set()

    for value in values:
        if value in valuesSet:
            print(f"Part 1. solution {value} * {2020-value} = {value * (2020 - value)}")
            break
        else:
            valuesSet.add(2020 - value)

def part2(values):
    values.sort()

    for value in values:
        leftPtr = 0
        rightPtr = len(values) - 1

        while(leftPtr < rightPtr):
            if values[leftPtr] + values[rightPtr] + value == 2020:
                print(f"Part 2. solution {value} * {values[leftPtr]} * {values[rightPtr]} = {value * values[leftPtr] * values[rightPtr]}")
                return
            elif values[leftPtr] + values[rightPtr] + value > 2020 - value:
                rightPtr -= 1
            else:
                leftPtr += 1

part1(values)
part2(values)
