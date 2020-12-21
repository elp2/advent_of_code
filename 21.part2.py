from collections import defaultdict

def return_default():
    return 0

def dd():
    return defaultdict(return_default)


CHALLENGE_DAY = "21"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
SAMPLE_EXPECTED = 5
# SAMPLE_EXPECTED = 


def parse_lines(raw):
    # Groups.
    # split = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), split))

    split = raw.split("\n")

    adict = {}
    words = defaultdict(return_default)
    for line in split:
        ls = line.strip().split(" (")
        ingredients = set(ls[0].split(" "))
        for i in ingredients:
            words[i] += 1
        c = ls[1]
        c = c[c.index(" ") + 1: -1]
        c = c.replace(",", "")
        allergens = c.split(" ")
        for a in allergens:
            print(a)
            if a in adict:
                known = adict[a]
                adict[a] = known & ingredients
                print(a, adict[a])
            else:
                adict[a] = ingredients
        print(line, adict)
    
    return adict, words
    # return split # raw
    # return list(map(lambda l: l.split(" "), split)) # words.
    # return list(map(int, split))
    # return list(map(lambda l: l.strip(), split)) # beware leading / trailing WS

def solve(raw):
    adict, words = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0

    allwords = set(words.keys())
    for v in adict.values():
        allwords -= v

    solved = {}
    changed = True
    while changed:
        changed = False

        for a, poss in adict.items():
            if len(poss) == 1:
                solved[a] = list(poss)[0]
                del(adict[a])
                for k, v in adict.items():
                    if k != a:
                        v -= poss
                changed = True
                break
    
    ret = []
    sk = list(solved.keys())
    sk.sort()
    for key in sk:
        ret.append(solved[key])
    return ",".join(ret)

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
    assert sample == "mxmxvkd,sqjhc,fvjkl"
    print("*** SAMPLE PASSED ***")

solved = solve(REAL)
print("SOLUTION: ", solved)
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
# assert solved
