passwords = []
with open('day2input.txt', 'r') as file:
    for item in file.readlines():
        passwords.append(item.strip())


def part1(passwords):
    validPasswordCount = 0
    for element in passwords:
        rule, password = element.split(':')
        rule = rule.split(' ')
        lowerLimit = int(rule[0].split('-')[0])
        upperLimit = int(rule[0].split('-')[1])
        letterCount = password.count(rule[1])

        if letterCount >= lowerLimit and letterCount <= upperLimit:
            validPasswordCount += 1
    
    print(f"Part 1. solution {validPasswordCount}")

def part2(passwords):
    validPasswordCount = 0
    for element in passwords:
        positions, password = element.split(':')
        positions = positions.split(' ')
        firstIndex = int(positions[0].split('-')[0])
        secondIndex = int(positions[0].split('-')[1])
        letter = positions[1]

        if (password[firstIndex] == letter and not password[secondIndex] == letter) or (not password[firstIndex] == letter and password[secondIndex] == letter):
            validPasswordCount += 1
    
    print(f"Part 2. solution {validPasswordCount}")

part1(passwords)
part2(passwords)