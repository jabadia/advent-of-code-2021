from utils.test_case import TestCase
from d9_input import INPUT

TEST_CASES = [
    TestCase("""
2199943210
3987894921
9856789892
8767896789
9899965678
""", 15),
]

NEIGHBOURS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def solve(input):
    heightmap = [[int(h) for h in row] for row in input.strip().split('\n')]
    rows = len(heightmap)
    cols = len(heightmap[0])

    def risk(row, col):
        height = heightmap[row][col]
        for delta_row, delta_col in NEIGHBOURS:
            if 0 <= row + delta_row < rows and 0 <= col + delta_col < cols:
                if height >= heightmap[row + delta_row][col + delta_col]:
                    return 0
        return height + 1

    return sum(risk(row, col) for row in range(rows) for col in range(cols))


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
