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
""", 2188189693529)
]


@timing
def solve(input):
    polymer, rules = input.strip().split('\n\n')
    rules = dict(rule.split(' -> ') for rule in rules.strip().split('\n'))

    first = polymer[0]
    last = polymer[-1]
    polymer = Counter(c0 + c1 for c0, c1 in zip(polymer[:-1], polymer[1:]))

    for step in range(40):
        new_polymer = Counter()
        for pair, count in polymer.items():
            insertion = rules.get(pair)
            if insertion:
                new_polymer[pair[0] + insertion] += count
                new_polymer[insertion + pair[1]] += count
            else:
                new_polymer[pair] += count
        polymer = new_polymer

    element_count = Counter()
    for pair, count in polymer.items():
        element_count[pair[0]] += count
        element_count[pair[1]] += count

    element_count[first] += 1
    element_count[last] += 1

    freq = element_count.most_common()
    return freq[0][1] // 2 - freq[-1][1] // 2


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
