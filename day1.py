values = []
with open('day1input.txt', 'r') as file:
    for item in file.readlines():
        values.append(int(item.strip()))

def part1():
    valuesSet = set()

    for value in values:
        if value in valuesSet:
            print(f"Part 1. solution {value} * {2020-value} = {value * (2020 - value)}")
            break
        else:
            valuesSet.add(2020 - value)

def part2():
    values.sort()

    for i in range(len(values)):
        leftPtr = 0
        rightPtr = len(values) - 1

        while(leftPtr < rightPtr):
            if values[leftPtr] + values[rightPtr] + values[i] == 2020:
                print(f"Part 2. solution {values[i]} * {values[leftPtr]} * {values[rightPtr]} = {values[i] * values[leftPtr] * values[rightPtr]}")
                return
            elif values[leftPtr] + values[rightPtr] + values[i] > 2020 - values[i]:
                rightPtr -= 1
            else:
                leftPtr += 1

part1()
part2()
