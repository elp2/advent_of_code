from collections import defaultdict

def return_default():
    return 0

def dd():
    return defaultdict(return_default)


CHALLENGE_DAY = "14"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample2.txt").read()
SAMPLE_EXPECTED = 208
# SAMPLE_EXPECTED =


def transform_loc(mask, loc):
    ret = ""
    for i in range(len(mask)):
        here = mask[i]
        if here == "0":
            ret += loc[i]
        elif here == "1":
            ret += "1"
        elif here == "X":
            ret += "X"
    assert len(ret) == len(mask)
    print("Loc ", loc, " -> ", ret)
    return ret

def parse_lines(raw):
    # Groups.
    # split = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), split))

    split = raw.split("\n")
    return split


    # return split # raw
    # return list(map(lambda l: l.split(" "), split)) # words.
    # return list(map(int, split))
    # return list(map(lambda l: l.strip(), split)) # beware leading / trailing WS

def read_mask(line):
    line = line.strip()
    maskstr = line.split(" = ")[1]
    return maskstr

def parse_mem(line):
    line = line.strip()
    val = int(line.split(" = ")[1])
    loc = line[line.index("[") + 1:line.index("]")]
    loc = bin(int(loc))
    loc = loc.replace("0b", "")
    while len(loc) != 36:
        loc = "0" + loc
    return loc, val

def get_ops(lines):
    mask = None
    ops = []
    for line in lines:
        if line.startswith("mask"):
            mask = read_mask(line)
        else:
            loc, val = parse_mem(line)
            loc = transform_loc(mask, loc)
            ops.append((loc, val))
    return ops

def merge_locs(a, b):
    assert len(a) == len(b)
    if a == b:
        return None
    ret = ""
    for i in range(len(a)):
        ca = a[i]
        cb = b[i]
        if ca == "X" and cb in "01":
            if cb == "0":
                ret += "1"
            else:
                ret += "0"
        elif ca in "01" and cb in "01":
            if ca != cb:
                # Can never overlap.
                return a
            else:
                ret += ca # TODO
        elif ca in "01X" and cb == "X":
            ret += ca
        else:
            assert False

    diffs = 0
    for i in range(len(ret)):
        ri = ret[i]
        bi = b[i]
        if ri in "X" and bi in "01":
            diffs += 1
        elif ri in "01" and bi in "01" and ri != bi:
            diffs += 1
        elif ri in "X01" and bi in "X":
            diffs += 0
        elif ri == bi:
            diffs += 0
        else:
            assert False
    
    if diffs == 0:
        return None
    assert len(ret) == len(a)
    return ret

pairs = [["010", "010"], ["0X0", "010"], ["XXX", "111"], ["01X", "100"]]
for a, b in pairs:
    print(a, b, merge_locs(a, b))

print("-----")


def memory_value(ops, i):
    orig_loc, val = ops[i]
    loc = orig_loc
    for j in range(i + 1, len(ops)):
        bloc, _ = ops[j]
        loc = merge_locs(loc, bloc)
        if loc is None:
            print("Loc ", orig_loc, " NONED")
            return 0
    
    print(orig_loc, loc)
    xes = loc.count("X")
    ret = val * pow(2, xes)
    if val == 126092:
        assert True
    return ret


def sum_memory(ops):
    ret = 0
    for i in range(len(ops)):
        ret += memory_value(ops, i)
    
    return ret
        

def solve_fast(raw):
    # '0b1111111111001001' = max loc seen
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ops = get_ops(parsed)
    return sum_memory(ops)

def get_xpositions(loc):
    pos = []
    xes = loc.count("X")
    upto = pow(2, xes)
    p = 0
    while p < upto:
        here = list(loc)
        istr = bin(p)
        istr = istr[2:]
        while len(istr) != xes:
            istr = "0" + istr
        i = 0
        for j in range(len(here)):
            if here[j] == "X":
                here[j] = istr[i]
                i += 1
        pos.append(int("".join(here), 2))
        p += 1
    return pos

def solve(raw):
    parsed = parse_lines(raw)
    ops = get_ops(parsed)
    memory = defaultdict(return_default)
    for i in range(len(ops)):
        loc, val = ops[i]
        xpos = get_xpositions(loc)
        for x in xpos:
            memory[x] = val
        print("i", len(memory))
    return sum(memory.values())




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

sample = solve(SAMPLE)
if SAMPLE_EXPECTED is None:
    print("*** SKIPPING SAMPLE! ***")
else:
    assert sample == SAMPLE_EXPECTED
    print("*** SAMPLE PASSED ***")

solved = solve(REAL)
if solved not in [2001667225974]:
    print("!!!!! SOLVED  !!!!!!")
    import pandas as pd
    df=pd.DataFrame([str(solved)])
    df.to_clipboard(index=False,header=False)
    print("COPIED TO CLIPBOARD") # 2001667225974 too low
    assert False
    # assert solved
else:
    print("BROKEN: ", solved)
