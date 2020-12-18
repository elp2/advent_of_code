from collections import defaultdict

def return_default():
    return 0

def dd():
    return defaultdict(return_default)


CHALLENGE_DAY = "18"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
SAMPLE_EXPECTED =  13632
# SAMPLE_EXPECTED = 71 + 51 + 26 + 437 + 12240 +


def parse_lines(raw):
    # Groups.
    # split = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), split))

    split = raw.split("\n")

    return split # raw
    # return list(map(lambda l: l.split(" "), split)) # words.
    # return list(map(int, split))
    # return list(map(lambda l: l.strip(), split)) # beware leading / trailing WS


from collections import deque


def calc(line):
    line = line.replace("(", " ( ")
    line = line.replace(")", " ) ")
    tokens = line.split(" ")
    tokens = list(filter(lambda t: t, tokens))
    return calc_tokens(tokens)


def calc_tokens(tokens):
    print("CT!: ", tokens)
    q = []
    for i, t in enumerate(tokens):
        print(t, q)
        t = str(t)
        ops = []      
        if t in "+*":
            q.append(t)
        elif t == "(":
            q.append(t)
            continue
        elif t == ")":
            while True:
                h = q.pop()
                if h == "(":
                    break
                ops.append(h)

        else:
            num = int(t)
            if len(q) and q[-1] in "+*":
                ops.append(num)
                ops.append(q.pop())
                ops.append(q.pop())
            else:
                ops = [num]

        if len(ops) == 1:
            q.append(ops[0])
        elif len(ops) == 3:
            a, op, b = ops
            if op == "+":
                q.append(a + b)
            elif op == "*":
                q.append(a * b)
            else:
                assert False

    if len(q) != 1:
        return calc_tokens(q)
    return q[0]


def solve(raw):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.

    ret = 0
    for l in parsed:
        calced = calc(l)
        ret += calced
        print("!!! ", l, " => ", calced)
        print("-----------------")
    return ret

def test_parsing(lines):
    if isinstance(lines, list):
        for i in range(min(5, len(lines))):
            print(lines[i])
    elif isinstance(lines, dict) or isinstance(lines, defaultdict):
        nd = {}
        for k in list(lines.keys())[0: 5]:
            print("\"" + k + "\": " + str(lines[k]))
test_parsing(parse_lines(SAMPLE))
print("^^^^^^^^^PARSED SAMPLE SAMPLE^^^^^^^^^")

# 1 + 2 * 3 + 4 * 5 + 6
# 1 + (2 * 3) + (4 * (5 + 6))
# 2 * 3 + (4 * 5)
# 5 + (8 * 3 + 9 + 3 * 4 * 3)
# 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))

sample = solve(SAMPLE)
if SAMPLE_EXPECTED is None:
    print("*** SKIPPING SAMPLE! ***")
else:
    assert sample == SAMPLE_EXPECTED
    print("*** SAMPLE PASSED ***")

solved = solve(REAL)
print("SOLUTION: ", solved)
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
# assert solved
