from utils.test_case import TestCase
from d7_input import INPUT

TEST_CASES = [
    TestCase("""
16,1,2,0,4,2,7,1,2,14
""", 37),
]


def solve(input):
    positions = sorted(int(n) for n in input.strip().split(','))
    median = positions[len(positions) // 2]
    return sum(abs(pos-median) for pos in positions)


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
