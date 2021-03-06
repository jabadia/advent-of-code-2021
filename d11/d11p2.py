# started 2021-12-11T21:46:37.058543
from utils.test_case import TestCase
from d11_input import INPUT
from utils.timing import timing

TEST_CASES = [
    TestCase("""
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
""", 195),
]

@timing
def solve(input):
    energy = [
        [int(n) for n in list(row)]
        for row in input.strip().split('\n')
    ]
    height = len(energy)
    width = len(energy[0])

    def neighbours(row, col):
        for r in range(row - 1, row + 2):
            if 0 <= r < height:
                for c in range(col - 1, col + 2):
                    if 0 <= c < width:
                        yield r, c

    step = 1
    while True:
        # increase energy
        flashes = []
        for row in range(height):
            for col in range(width):
                energy[row][col] += 1
                if energy[row][col] == 10:
                    flashes.append((row, col))

        # flash
        flashed = []
        while flashes:
            row, col = flashes.pop()
            flashed.append((row, col))
            for r, c in neighbours(row, col):
                energy[r][c] += 1
                if energy[r][c] == 10:
                    flashes.append((r, c))

        if len(flashed) == height * width:
            return step

        # reset to 0
        while flashed:
            row, col = flashed.pop()
            energy[row][col] = 0

        step += 1


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
