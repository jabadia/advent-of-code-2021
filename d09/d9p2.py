import math
from utils.test_case import TestCase
from d9_input import INPUT


TEST_CASES = [
    TestCase("""
2199943210
3987894921
9856789892
8767896789
9899965678
""", 1134),
]

NEIGHBOURS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def solve(input):
    heightmap = [[int(h) for h in row] for row in input.strip().split('\n')]
    rows = len(heightmap)
    cols = len(heightmap[0])

    def floodfill(row, col):
        height = heightmap[row][col]
        if height == 9:
            return 0
        heightmap[row][col] = 9
        size = 1
        for delta_row, delta_col in NEIGHBOURS:
            if 0 <= row + delta_row < rows and 0 <= col + delta_col < cols:
                size += floodfill(row + delta_row, col + delta_col)
        return size


    basin_sizes = []
    for r in range(rows):
        for c in range(cols):
            if heightmap[r][c] != 9:
                basin_sizes.append(floodfill(r, c))

    return math.prod(sorted(basin_sizes)[-3:])


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
