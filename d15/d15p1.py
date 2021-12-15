# started 2021-12-15T06:00:08.681156
import heapq
from colorama import Fore, Style
from utils.test_case import TestCase
from d15_input import INPUT

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
""", 40),
]


def print_solution(risk_levels, visited):
    for j, row in enumerate(risk_levels):
        for i, n in enumerate(row):
            if (j, i) in visited:
                print(Style.BRIGHT, end='')
            else:
                print(Fore.WHITE, end='')
            print(n, end='')
            print(Style.RESET_ALL, end='')
        print()
    print()


def solve(input):
    risk_levels = [
        [int(n) for n in list(row)]
        for row in input.strip().split('\n')
    ]
    height = len(risk_levels)
    width = len(risk_levels[0])

    start = (0, 0)
    target = (height-1, width-1)

    def neighbours(pos):
        row, col = pos
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= row + dr < height and 0 <= col + dc < width:
                yield row + dr, col + dc

    queue = [(0, start)]
    visited = set()
    while queue:
        risk, pos = heapq.heappop(queue)
        visited.add(pos)
        if pos == target:
            return risk
        for neighbour in neighbours(pos):
            if neighbour not in visited:
                if (risk + risk_levels[neighbour[0]][neighbour[1]], neighbour) not in queue:
                    heapq.heappush(queue, (
                        risk + risk_levels[neighbour[0]][neighbour[1]],
                        neighbour,
                    ))

    return -1


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
