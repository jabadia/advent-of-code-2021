# started 2021-12-14T06:00:06.735749
from collections import Counter

from utils.test_case import TestCase
from d14_input import INPUT
from utils.timing import timing

TEST_CASES = [
    TestCase("""
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C    
""", 1588),
]


@timing
def solve(input):
    polymer, rules = input.strip().split('\n\n')
    rules = dict(rule.split(' -> ') for rule in rules.strip().split('\n'))

    for step in range(10):
        new_polymer = ''
        for c0, c1 in list(zip(polymer[:-1], polymer[1:])):
            pair = c0 + c1
            insertion = rules.get(pair, None)
            new_polymer += c0
            if insertion:
                new_polymer += insertion
        new_polymer += c1
        polymer = new_polymer

    freq = Counter(polymer).most_common()
    return freq[0][1] - freq[-1][1]


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
