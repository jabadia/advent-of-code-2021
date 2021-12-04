from itertools import filterfalse, tee
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
""", 230),
]


# from https://docs.python.org/dev/library/itertools.html#itertools-recipes
def partition(pred, iterable):
    """Use a predicate to partition entries into false entries and true entries"""
    # partition(is_odd, range(10)) --> 0 2 4 6 8   and  1 3 5 7 9
    t1, t2 = tee(iterable)
    return filterfalse(pred, t1), filter(pred, t2)


def filter_numbers(numbers, pos, use_most_common):
    # print(len(numbers), ' '.join(numbers), pos, use_most_common)
    if len(numbers) == 1:
        return numbers

    zeroes, ones = map(list, partition(lambda number: number[pos] == '1', numbers))
    if len(ones) >= len(zeroes):
        most_common, least_common = ones, zeroes
    else:
        most_common, least_common = zeroes, ones

    return filter_numbers(most_common if use_most_common else least_common, pos + 1, use_most_common)


def solve(input):
    numbers = input.strip().split()

    oxygen_generator_bits = filter_numbers(numbers, 0, use_most_common=True)
    co2_scrubber_bits = filter_numbers(numbers, 0, use_most_common=False)

    oxygen_generator_rating = int(''.join(oxygen_generator_bits), 2)
    co2_scrubber_rating = int(''.join(co2_scrubber_bits), 2)

    return oxygen_generator_rating * co2_scrubber_rating


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
