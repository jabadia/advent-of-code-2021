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
""", 26397),
]

POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

MATCHING = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}


def check_line(line):
    stack = []
    for c in line:
        if c in '[({<':
            stack.append(c)
        else:
            opening = stack.pop()
            if MATCHING[c] != opening:
                return POINTS[c]
    return 0


def solve(input):
    score = sum(check_line(line) for line in input.strip().split('\n'))
    return score


if __name__ == '__main__':
    for case in TEST_CASES:
        result = solve(case.case)
        case.check(result)

    print(solve(INPUT))
