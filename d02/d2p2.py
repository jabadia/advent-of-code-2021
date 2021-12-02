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
""", 900),
]


def solve(input):
    pos = (0, 0, 0)
    for move in input.strip().split('\n'):
        horizontal, depth, aim = pos
        match move.split(' '):
            case ['forward', units]:
                pos = (horizontal + int(units), depth + aim * int(units), aim)
            case ['up', units]:
                pos = (horizontal, depth, aim - int(units))
            case ['down', units]:
                pos = (horizontal, depth, aim + int(units))
            case _:
                assert False, 'bad direction'

    return pos[0] * pos[1]


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
