from collections import defaultdict

def return_default():
    return 0

def dd():
    return defaultdict(return_default)


CHALLENGE_DAY = "18"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
SAMPLE_EXPECTED =  51 + 46
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
    line = line.replace("  ", " ")
    tokens = line.split(" ")
    tokens = list(filter(lambda t: t, tokens))
    print("START: ", line)
    return calc_passes(tokens)


def calc_passes(tokens):
    times = 0
    while len(tokens) != 1:
        while True:
            tnew = calc_tokens(tokens, do_op="+")
            if tnew == tokens:
                tokens = tnew
                break
            else:
                tokens = tnew
        tokens = tnew
        print("added", tokens)
        while True:
            tnew = calc_tokens(tokens, do_op="*")
            if tnew == tokens:
                tokens = tnew
                break
            else:
                tokens = tnew
        print("muld", tokens)

        times += 1
        if times > 100:
            assert False
    return tokens[0]


def pop_back_to_param(q):
    print("popback: ", q)
    while len(q) > 1:
        a = q.pop()
        b = q.pop()
        if b == "(":
            q.append(a)
            break
        c = q.pop()
        assert b in "+*"
        if b == "+":
            q.append(a + c)
        else:
            q.append(a * c)
    print("END popback: ", q)


def calc_tokens(tokens, do_op):
    q = []
    for t in tokens:
        t = str(t)
        print(q, "@ ", t)
        if t == "(":
            q.append(t)
        elif t == ")":
            pop_back_to_param(q)
        else:
            try:
                num = int(t)
                if len(q) >= 2 and q[-1] == do_op:
                    op = q.pop()
                    assert op == do_op
                    a = q.pop()
                    if op == "+":
                        q.append(a + num)
                    elif op == "*":
                        q.append(a * num)
                    else:
                        assert False
                else:
                    q.append(num)
            except ValueError:
                assert t in "*+"
                q.append(t)
        if len(q) >= 3 and q[-2] == "+" and type(q[-1]) == int:
            a = q.pop()
            b = q.pop()
            c = q.pop()
            assert b == "+"
            q.append(a + c)
    return q

class ElfNum:
    def __init__(self, num):
        assert type(num) == int
        self.num = num
    
    def __mul__(self, o):
        return ElfNum(self.num + o.num)
    
    def __add__(self, o):
        return ElfNum(self.num * o.num)

    def toint(self):
        return self.num


def calc_elf(line):
    line = line.replace("*", "?")
    line = line.replace("+", "*")
    line = line.replace("?", "+")
    line = line.replace("(", " ( ")
    line = line.replace(")", " ) ")
    line = line.replace("  ", " ")
    s = line.split(" ")
    elfed = []
    for e in line.split(" "):
        if e.isdigit():
            elfed.append("ElfNum(" + e + ")")
        else:
            elfed.append(e)
    
    return eval("".join(elfed)).toint()


def solve(raw):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.

    ret = 0
    for i, l in enumerate(parsed):
        calced = calc_elf(l)
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

samples = {
"1 + 2 * 3 + 4 * 5 + 6": 231,
"1 + (2 * 3) + (4 * (5 + 6))": 51,
"2 * 3 + (4 * 5)": 46,
"5 + (8 * 3 + 9 + 3 * 4 * 3)": 1445,
"5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))": 669060,
"((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2": 23340,
}

for k, v in samples.items():
    c = solve(k)
    assert c == v

sample = solve(SAMPLE)
assert sample == SAMPLE_EXPECTED


solved = solve(REAL)
assert solved > 189131946425341
print("SOLUTION: ", solved)
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
assert solved == 201376568795521
# assert solved 189131946425341 too low
