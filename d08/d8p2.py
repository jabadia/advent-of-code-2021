from functools import reduce

from utils.test_case import TestCase
from d8_input import INPUT

DIGITS = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg',
}

for d, pattern in DIGITS.items():
    print(d, len(pattern), pattern)


TEST_CASES = [
    TestCase("""
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
""", 61229),
]


def find_first(seq, pred):
    return next(item for item in seq if pred(item))


def solve(input):
    total = 0
    for line in input.strip().split('\n'):
        patterns, output = line.split(' | ')
        patterns = [set(pattern) for pattern in patterns.split(' ')]
        output = [set(pattern) for pattern in output.split(' ')]

        solved = [None] * 10

        solved[1] = find_first(patterns, lambda digit: len(digit) == 2)
        solved[7] = find_first(patterns, lambda digit: len(digit) == 3)
        solved[8] = find_first(patterns, lambda digit: len(digit) == 7)
        solved[4] = find_first(patterns, lambda digit: len(digit) == 4)

        maybe_069 = [digit for digit in patterns if len(digit) == 6]
        solved[6] = find_first(maybe_069, lambda digit: len(digit & solved[1]) == 1)
        solved[9] = find_first(maybe_069, lambda digit: len(digit & solved[4]) == 4)
        solved[0] = find_first(maybe_069, lambda digit: digit != solved[9] and digit != solved[6])

        maybe_235 = [digit for digit in patterns if len(digit) == 5]
        solved[3] = find_first(maybe_235, lambda digit: len(digit & solved[1]) == 2)
        solved[5] = find_first(maybe_235, lambda digit: len(digit & solved[6]) == 5)
        solved[2] = find_first(maybe_235, lambda digit: digit != solved[3] and digit != solved[5])

        total += reduce(lambda acc, digit: 10 * acc + solved.index(digit), output, 0)

    return total


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
