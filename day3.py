layout = []
with open('day3input.txt', 'r') as file:
    for item in file.readlines():
        layout.append(item.strip())

part2Slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

def part1():
    trees = countSlopeTrees(3, 1)

    print(f"Part 1. solution {trees}")
   
def part2(slopes):
    result = 1
    for slope in slopes:
        trees = countSlopeTrees(slope[0], slope[1])
        result *= trees
    
    print(f"Part 2. solution {result}")

def countSlopeTrees(deltaX, deltaY):
    x = 0
    y = 0
    trees = 0

    for _ in range(0, len(layout), deltaY):
        x = (x + deltaX) % 31
        y = (y + deltaY) % 323
        if layout[y][x] == '#':
            trees += 1

    return trees
    

    

part1()
part2(part2Slopes)
