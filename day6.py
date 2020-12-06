groupAnswers = []
groupForms = []

with open('day6input.txt', 'r') as file:
    for item in file.readlines():
        if item == "\n":
            groupAnswers.append([data for data in groupForms])
            groupForms.clear()
        else:
            groupForms.append(item.strip())

def part1():
    uniqueCountPerGroup = []
    answerCount = set()

    for answerList in groupAnswers:
        for listItem in answerList:
            for answer in listItem:
                answerCount.add(answer)
        
        uniqueCountPerGroup.append(len(answerCount))
        answerCount.clear()

    print(f"Part 1. solution {sum(uniqueCountPerGroup)}")
   
def part2():
    allYesPerGroup = []
    answerCount = {}

    for answerList in groupAnswers:
        for listItem in answerList:
            for answer in listItem:
                if answer in answerCount:
                    answerCount[answer] += 1
                else:
                    answerCount[answer] = 1
        
        allYesPerGroup.append(sum([1 for x in answerCount.keys() if answerCount[x] == len(answerList)]))
        answerCount.clear()
        
        
    print(f"Part 2. solution {sum(allYesPerGroup)}")


part1()
part2()