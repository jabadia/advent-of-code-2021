from collections import Counter
from utils.test_case import TestCase
from d6_input import INPUT

TEST_CASES = [
    TestCase("""
3,4,3,1,2
""", 26984457539),
]


def solve(input):
    fishes = Counter(int(n) for n in input.strip().split(','))

    for time in range(256):
        spawn = fishes[0]
        for cycle in range(8):
            fishes[cycle] = fishes[cycle + 1]
        fishes[8] = spawn
        fishes[6] += spawn

    return sum(fishes.values())


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
