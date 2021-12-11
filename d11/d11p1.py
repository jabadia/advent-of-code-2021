# started 2021-12-11T21:46:37.058543
from utils.test_case import TestCase
from d11_input import INPUT

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
""", 1656),
]


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
                        yield (r, c)

    def print_energy(energy):
        for row in energy:
            print(''.join(str(n) if n != 9 else '*' for n in row))

    flash_count = 0
    for step in range(100):
        # increase energy
        flashes = []
        for row in range(height):
            for col in range(width):
                energy[row][col] += 1
                if energy[row][col] == 10:
                    flashes.append((row, col))

        # print_energy(energy)

        # flash
        flashed = []
        while flashes:
            row, col = flashes.pop()
            flash_count += 1
            flashed.append((row,col))
            for r, c in neighbours(row, col):
                energy[r][c] += 1
                if energy[r][c] == 10:
                    flashes.append((r, c))

        while flashed:
            row, col = flashed.pop()
            energy[row][col] = 0

    return flash_count


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
