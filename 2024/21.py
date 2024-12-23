from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations, product
from functools import reduce, cmp_to_key
from operator import add, mul, itemgetter, attrgetter
import os
from parse import parse
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)
from aoc_elp import *

######################
SAMPLE_EXPECTED = 126384
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def parse_group(group):
    lines = group.split("\n")
    ret = []
    for y, line in enumerate(lines):
        line = line.strip()
        assert len(line) != 0

        split = line.split(" ")

        for x, xc in enumerate(split):
            pass

        assert len(split) != 0
        ret.append(split)

    return ret


def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # Do something with the groups.

    return raw.split("\n")

def buttonify(s):
    split = s.split("\n")
    ret = {}
    for y, row in enumerate(split):
        for x, xc in enumerate(row):
            if xc != " ":
                ret[xc] = Pos(x, y)
    return ret



# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+
# When the robot arrives at the numeric keypad, its robotic arm is pointed at the A button in the bottom right corner.
numeric = buttonify("""789
456
123
 0A""")
numeric2 = {"7": Pos(0, 0), "8": Pos(1, 0), "9": Pos(2,0), "4": Pos(0,1), "5": Pos(1,1), "6": Pos(2,1), "1": Pos(0,2), "2": Pos(1, 2), "3": Pos(2,2), "0": Pos(1, 3), "A": Pos(2, 3)}
for k,v in numeric.items():
    print(k, v, numeric2[k])
assert numeric == numeric2

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+
directional2 = {"^": Pos(1, 0), "A": Pos(2,0), "<": Pos(0, 1), "v": Pos(1, 1), ">": Pos(2, 1)}
directional = buttonify(""" ^A
<v>""")
assert directional2 == directional

def button_sequences(char, buttons, startpos):
    q = deque()
    target = buttons[char]
    q.append((startpos, "", target.x - startpos.x, target.y - startpos.y))
    ret = []
    while q:
        at, seq, dx, dy = q.popleft()
        # print(at, seq, dx, dy)
        if at not in buttons.values():
            continue
        if at == target:
            assert dx == dy and dy == 0
            ret.append(seq + "A")
            continue
        if dx > 0:
            q.append((at.add(Vel(1, 0)), seq + ">", dx - 1, dy))
        if dx < 0:
            q.append((at.add(Vel(-1, 0)), seq + "<", dx + 1, dy))
        if dy > 0:
            q.append((at.add(Vel(0, 1)), seq + "v", dx, dy - 1))
        if dy < 0:
            q.append((at.add(Vel(0, -1)), seq + "^", dx, dy + 1))
    return ret, target

bs = button_sequences("7", numeric, numeric["3"])
print("3->7", bs)

def multichar_sequences(chars, buttons, startpos):
    ret = []
    for c in chars:
        cseqs, startpos = button_sequences(c, buttons, startpos)
        nret = []
        for cs in cseqs:
            if not len(ret):
                ret = ['']
            for r in ret:
                nret.append(r + cs)

        assert len(cseqs) * len(ret) == len(nret)
        ret = list(set(nret))

    return ret

# msq = multichar_sequences("<^A", directional, directional["A"])


def directional_sequence(directions, startpos):
    at = startpos
    seq = []
    for dir in directions:
        if dir == ",":
            continue
        next = directional[dir]
        dx = next.x - at.x
        dy = next.y - at.y
        here = ""
        if dy < 0 :
            vert = (-1 * dy) * "^"
        else:
            vert = dy * "v"
        
        if dx > 0:
            horiz = dx * ">"
        else:
            horiz = (-1 * dx) * "<"
        
        if dx > 0:
            here = horiz + vert
        else:
            here = vert + horiz
        
        here = here + "A"
        # print(directions, here)
        seq.append(here)
        at = next
    print(seq)
    return "".join(seq), at

def numeric_sequence(code, startpos):
    at = startpos
    seq = []
    for number in code:
        next = numeric[number]
        dx = next.x - at.x
        dy = next.y - at.y
        here = ""
        if dy < 0 :
            vert = (-1 * dy) * "^"
        else:
            vert = dy * "v"
        
        if dx > 0:
            horiz = dx * ">"
        else:
            horiz = (-1 * dx) * "<"

        # if dy == 1 and dx == 1:
        #     # we can choose to do them in either order. (>v or v>) Pick one that convers better without backtracking next one
        #     here = horiz + vert
        #     # here = here + ">v"
        # elif dy == -1 and dx == -1:    
        #     here = vert + horiz
        #     # here = here + "^<"
        if dx > 0: # vv, hv, hh, vh
            if dx == dy:
                here = vert + horiz
            here = horiz + vert
        else:
            if dx == dy:
                horiz + vert
            here = vert + horiz
        
        here = here + "A"
        # print(number, here)
        seq.append(here)
        at = next
    print(seq)
    return "".join(seq), at

def shortest_seq(chars):

    depth = 0

    ret = []
    rec = [chars]
    for depth in range(3):
        if depth == 0:
            buttons = numeric
            startpos = numeric["A"]
        else:
            buttons = directional
            startpos = directional["A"]
        here = []
        for r in rec:
            rh = multichar_sequences(r, buttons, startpos)
            here = here + rh
        
        here = list(set(here))
        # print(depth, "<- depth", here)
        rec = here
    
    lens = set([len(x) for x in here])

    return min(lens)

# shortest_seq("379A")

def solve(raw):
    parsed = parse_lines(raw)
    print(parsed)

    ret = 0
    numeric_pos = numeric["A"]
    num_dir = 2
    dps = [directional["A"] for _ in range(num_dir)]

    for code in parsed:
        minlen = shortest_seq(code)

        a, b = minlen, int(code[:3])
        print(code, a, b)
        ret += a * b

    return ret

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)

    s1 = solve("379A")
    assert s1 == 64 * 379, "Sample Result %s != %s expected" % (s1, 64 * 379)
    print("\n*** SAMPLE PASSED ***\n")

    # sample = solve(SAMPLE)
    # assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
