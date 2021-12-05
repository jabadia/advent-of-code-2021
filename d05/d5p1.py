from collections import defaultdict

from utils.test_case import TestCase
from d5_input import INPUT

TEST_CASES = [
    TestCase("""
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
""", 5),
]


def solve(input):
    lines = input.strip().split('\n')
    world = defaultdict(int)
    for line in lines:
        line = line.replace(' -> ', ',')
        x0, y0, x1, y1 = [int(n) for n in line.split(',')]
        [x0, x1] = sorted([x0, x1])
        [y0, y1] = sorted([y0, y1])
        if x0 == x1:
            for y in range(y0, y1 + 1):
                world[(x0, y)] += 1
        elif y0 == y1:
            for x in range(x0, x1 + 1):
                world[(x, y0)] += 1
        else:
            pass  # not horizontal or vertical

    return sum(line_count > 1 for line_count in world.values())


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
