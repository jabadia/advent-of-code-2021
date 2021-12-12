# started 2021-12-12T22:40:45.589478
from collections import defaultdict

from utils.test_case import TestCase
from d12_input import INPUT

TEST_CASES = [
    TestCase("""
start-A
start-b
A-c
A-b
b-d
A-end
b-end    
""", 36),
    TestCase("""
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc
""", 103),
    TestCase("""
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW
""", 3509)
]


def solve(input):
    graph = defaultdict(set)
    for edge in input.strip().split('\n'):
        v0, v1 = edge.split('-')
        graph[v0].add(v1)
        graph[v1].add(v0)

    graph = dict(graph)

    paths = []
    queue = [('start', [], False)]
    while queue:
        v, path, already_visited_small_cave_twice = queue.pop()
        for next in graph[v]:
            if next == 'end':
                paths.append(path)
            elif next == 'start':
                continue
            elif next == next.lower() and next in path:
                if already_visited_small_cave_twice:
                    continue
                else:
                    queue.append((next, path + [next], True))
            else:
                queue.append((next, path + [next], already_visited_small_cave_twice))

    return len(paths)


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
