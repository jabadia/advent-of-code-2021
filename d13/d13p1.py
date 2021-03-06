# started 2021-12-13T06:00:02.353857
from utils.test_case import TestCase
from d13_input import INPUT

TEST_CASES = [
    TestCase("""
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5    
""", 17),
]


def solve(input):
    dots, fold_instructions = input.strip().split('\n\n')
    paper = {
        tuple(map(int, dot.split(',')))
        for dot in dots.strip().split('\n')
    }

    for instruction in fold_instructions.strip().split('\n'):
        match instruction.split('='):
            case ('fold along x', fold_x):
                fold_x = int(fold_x)
                for x, y in paper.copy():
                    assert fold_x != x
                    if x > fold_x:
                        paper.remove((x, y))
                        paper.add((fold_x - (x - fold_x), y))
            case ('fold along y', fold_y):
                fold_y = int(fold_y)
                for x, y in paper.copy():
                    assert fold_y != y
                    if y > fold_y:
                        paper.remove((x, y))
                        paper.add((x, fold_y - (y - fold_y)))
        break
    return len(paper)


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
