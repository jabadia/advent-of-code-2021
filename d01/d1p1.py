from utils.test_case import TestCase
from d1_input import INPUT

TEST_CASES = [
    TestCase("""
199
200
208
210
200
207
240
269
260
263
""", 7),
]


def solve(input):
    depths = [int(line) for line in input.strip().split('\n') if line]
    increases = [d0 < d1 for d0, d1 in zip(depths[:-1], depths[1:])]
    return sum(increases)


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
