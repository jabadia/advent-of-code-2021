from utils.test_case import TestCase
from d2_input import INPUT

TEST_CASES = [
    TestCase("""
forward 5
down 5
forward 8
up 3
down 8
forward 2
""", 150),
]


def solve(input):
    pos = (0, 0)
    for move in input.strip().split('\n'):
        direction, amount = move.split(' ')
        amount = int(amount)
        horizontal, depth = pos
        if direction == 'forward':
            pos = (horizontal + amount, depth)
        elif direction == 'up':
            pos = (horizontal, depth - amount)
        elif direction == 'down':
            pos = (horizontal, depth + amount)
        else:
            assert False, 'bad direction'

    return pos[0] * pos[1]


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
