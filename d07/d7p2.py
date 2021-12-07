from utils.test_case import TestCase
from d7_input import INPUT

TEST_CASES = [
    TestCase("""
16,1,2,0,4,2,7,1,2,14
""", 168),
]


def fuel(positions, align):
    diff = [abs(pos-align) for pos in positions]
    f = [sum(range(d+1)) for d in diff]
    return sum(f)


def solve(input):
    positions = [int(n) for n in input.strip().split(',')]
    return min(fuel(positions, pos) for pos in range(min(positions), max(positions)))


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
