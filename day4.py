passports = []
passportData = []

with open('day4input.txt', 'r') as file:
    for item in file.readlines():
        if item == "\n":
            passports.append([data for data in passportData])
            passportData.clear()
        else:
            passportData.append(item.strip())

mandatoryFields = set([
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
])

eyeColors = [
    'amb',
    'blu',
    'brn',
    'gry',
    'grn',
    'hzl',
    'oth'
]

allowedSymbols = [
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    'a',
    'b',
    'c',
    'd',
    'e',
    'f'
]

numbers = [
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9'
]

def part1():
    validPasswords = 0

    for passport in passports:
        passportFields = set()
        for data in passport:
            for item in [field for field in mandatoryFields if data.find(field) != -1]:
                passportFields.add(item) 
        if mandatoryFields.issubset(passportFields):
            validPasswords += 1

    print(f"Part 1. solution {validPasswords}")

def part2():
    validPasswords = 0

    for passport in passports:
        passportFields = set()
        for data in passport:
            for item in data.split(' '):
                key = item.split(':')[0]
                value = item.split(':')[1]

                if key == 'byr' and validateByr(value):
                    passportFields.add(key)
                elif key == 'iyr' and validateIyr(value):
                    passportFields.add(key)
                elif key == 'eyr' and validateEyr(value):
                    passportFields.add(key)
                elif key == 'hgt' and validateHgt(value):
                    passportFields.add(key)
                elif key == 'hcl' and validateHcl(value):
                    passportFields.add(key)
                elif key == 'ecl' and validateEcl(value):
                    passportFields.add(key)
                elif key == 'pid' and validatePid(value):
                    passportFields.add(key)
    
        if mandatoryFields.issubset(passportFields):
            validPasswords += 1

    print(f"Part 2. solution {validPasswords}")

def validateByr(value):
    if 1920 <= int(value) <= 2002:
        return True
    else:
        return False

def validateIyr(value):
    if 2010 <= int(value) <= 2020:
        return True
    else:
        return False

def validateEyr(value):
    if 2020 <= int(value) <= 2030:
        return True
    else:
        return False

def validateHgt(value):
    cmPos = value.find('cm')
    inPos = value.find('in')
    
    if cmPos != -1:
        if 150 <= int(value[:cmPos]) <= 193:
            return True
    elif inPos != -1:
        if 59 <= int(value[:inPos]) <= 76:
            return True
    return False
        

def validateHcl(value):
    if value[0] == '#' and len(value) == 7:
        for symbol in value[1:]:
            if not symbol in allowedSymbols:
                break
        else:
            return True
    return False

def validateEcl(value):
    if value in eyeColors:
        return True
    else:
        return False

def validatePid(value):
    if len(value) == 9:
        for symbol in value:
            if symbol not in numbers:
                break
        else:
            return True
    return False

part1()
part2()