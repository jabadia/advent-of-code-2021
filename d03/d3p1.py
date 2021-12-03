from utils.test_case import TestCase
from d3_input import INPUT

TEST_CASES = [
    TestCase("""
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""", 198),
]


def solve(input):
    columns = zip(*input.strip().split())
    gamma_bits = [
        '0' if column.count('0') > len(column) // 2 else '1'
        for column in columns
    ]
    epsilon_bits = ['0' if gamma_bit == '1' else '1' for gamma_bit in gamma_bits]
    gamma = int(''.join(gamma_bits), 2)
    epsilon = int(''.join(epsilon_bits), 2)
    return gamma * epsilon


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
