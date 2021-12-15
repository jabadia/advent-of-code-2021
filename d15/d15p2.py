# started 2021-12-15T06:00:08.681156
import heapq
from utils.test_case import TestCase
from d15_input import INPUT

from utils.timing import timing

TEST_CASES = [
    TestCase("""
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
""", 315),
]


# @timing
def solve(input):
    rows = input.strip().split('\n')
    width = len(rows[0])
    height = len(rows)
    risk_levels = [
        [
            ((int(n) + i // width + j // height - 1) % 9) + 1
            for i, n in enumerate(list(row) * 5)
        ]
        for j, row in enumerate(rows * 5)
    ]

    width *= 5
    height *= 5

    def neighbours(pos):
        row, col = pos
        for delta_row, delta_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= row + delta_row < height and 0 <= col + delta_col < width:
                yield row + delta_row, col + delta_col

    target = (height - 1, width - 1)

    start = (0, 0)
    queue = [(0, start)]
    visited = {start}
    while queue:
        risk, pos = heapq.heappop(queue)
        if pos == target:
            return risk
        for neighbour in neighbours(pos):
            if neighbour not in visited:
                visited.add(neighbour)
                heapq.heappush(queue, (risk + risk_levels[neighbour[0]][neighbour[1]], neighbour))

    return -1


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
