REAL={
    "A": {
        0: [1, 1, "B"],
        1: [0, -1, "D"],
    },
    "B": {
        0: [1, 1, "C"],
        1: [0, 1, "F"],
    },
    "C": {
        0: [1, -1, "C"],
        1: [0, -1, "A"],
    },
    "D": {
        0: [0, -1, "E"],
        1: [1, 1, "A"],
    },
    "E": {
        0: [1, -1, "A"],
        1: [0, 1, "B"],
    },
    "F": {
        0: [0, 1, "C"],
        1: [0, 1, "E"],
    },
}

REAL_STEPS=12302209
REAL_START="A"

SAMPLE={
    "A": {
        0: [1, 1, "B"],
        1: [0, -1, "B"],
    },
    "B": {
        0: [1, -1, "A"],
        1: [1, 1, "A"],
    },
}

from collections import defaultdict
def return_zero():
    return 0
def part1(state, transitions, steps):
    tape = defaultdict(return_zero)
    pos = 0
    ones = 0
    for _ in range(steps):
        here = tape[pos]
        new_here, direction, new_state = transitions[state][here]

        if here == 1 and new_here == 0:
            ones -= 1
        if here == 0 and new_here == 1:
            ones += 1

        tape[pos] = new_here
        pos += direction
        state = new_state
    print(ones)
    print(sum(tape.values()))
    return ones

assert 3 == part1("A", SAMPLE, 6)
part1(REAL_START, REAL, REAL_STEPS) # 1118384 high
 
