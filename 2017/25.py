
REAL_STEPS=12302209

a, b, c, d, e, f = range(6)
right = 1
left = -1

SAMPLE={
    (a, 0): [1, right, b],
    (a, 1): [0, left, b],
    (b, 0): [1, left, a],
    (b, 1): [1, right, a],
}

REAL= {
    (a, 0): [1, right, b],
    (a, 1): [0, left, d],
    (b, 0): [1, right, c],
    (b, 1): [0, right, f],
    (c, 0): [1, left, c],
    (c, 1): [1, left, a],
    (d, 0): [0, left, e],
    (d, 1): [1, right, a],
    (e, 0): [1, left, a],
    (e, 1): [0, right, b],
    (f, 0): [0, right, c],
    (f, 1): [0, right, e],
}

from collections import defaultdict
def return_zero():
    return 0


def part1(state, transitions, steps):
    tape = defaultdict(return_zero)
    pos = 0
    for _ in range(steps):
        here = tape[pos]
        new_here, direction, new_state = transitions[(state, here)]

        tape[pos] = new_here
        pos += direction
        state = new_state
    return sum(tape.values())


assert 3 == part1(a, SAMPLE, 6)
print(part1(a, REAL, REAL_STEPS)) # 1118384 high # 4100737 no # 633 YES
 
