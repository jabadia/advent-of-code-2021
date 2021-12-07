from utils.test_case import TestCase
from d7_input import INPUT

TEST_CASES = [
    TestCase("""
16,1,2,0,4,2,7,1,2,14
""", 168),
]


# arithmetic series: sum(range(n)) = n * (n-1) // 2

def fuel(positions, align):
    return sum(
        delta * (delta + 1) // 2
        for delta in
        (abs(pos - align) for pos in positions)
    )


def solve(input):
    positions = [int(n) for n in input.strip().split(',')]
    return min(
        fuel(positions, align)
        for align in range(min(positions), max(positions))
    )


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
