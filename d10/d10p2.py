from utils.test_case import TestCase
from d10_input import INPUT

TEST_CASES = [
    TestCase("""
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]    
""", 288957),
]

POINTS = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

MATCHING = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}


def check_line(line):
    stack = []
    for c in line:
        if c in '[({<':
            stack.append(c)
        else:
            opening = stack.pop()
            if MATCHING[opening] != c:
                return -1  # line is corrupted

    # line is incomplete
    score = 0
    while stack:
        opening = stack.pop()
        score = score * 5 + POINTS[MATCHING[opening]]

    return score


def solve(input):
    scores = sorted(check_line(line) for line in input.strip().split('\n'))
    scores = [score for score in scores if score != -1]
    return scores[len(scores) // 2]


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
