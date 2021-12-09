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


def solve(input):
    heightmap = [[int(h) for h in row] for row in input.strip().split('\n')]
    rows = len(heightmap)
    cols = len(heightmap[0])

    def neighbours(pos):
        for delta in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbour = pos[0] + delta[0], pos[1] + delta[1]
            if 0 <= neighbour[0] < rows and 0 <= neighbour[1] < cols:
                yield neighbour

    def floodfill(pos):
        if heightmap[pos[0]][pos[1]] == 9:
            return 0
        heightmap[pos[0]][pos[1]] = 9
        return 1 + sum(
            floodfill(neighbour)
            for neighbour in neighbours(pos)
        )

    basin_sizes = [
        floodfill((r, c))
        for r in range(rows)
        for c in range(cols)
        if heightmap[r][c] != 9
    ]

    return math.prod(sorted(basin_sizes)[-3:])


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
