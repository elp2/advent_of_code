from collections import defaultdict, deque
import re

CHALLENGE_DAY = "7"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
# SAMPLE_EXPECTED = 

def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), groups))
    
    lines = raw.split("\n")
    # return lines # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    # return list(map(int, lines))
    return list(map(lambda l: [l, False], lines)) # beware leading / trailing WS

def solve(raw):
    parsed = parse_lines(raw)

    wires = {}

    resolved = 0
    while resolved != len(parsed):
        for i in range(len(parsed)):
            rule, used = parsed[i]
            if used:
                continue
            
            eq, destination = rule.split(" -> ")
            terms = eq.split(" ")
            translated = []
            op = None
            for t in terms:
                if t in ["OR", "AND", "NOT", "RSHIFT", "LSHIFT"]:
                    translated.append(t)
                else:
                    try:
                        val = int(t)
                    except ValueError:
                        if t in wires:
                            val = wires[t]
                        else:
                            val = None
                    translated.append(val)
            if len(translated) == 1:
                val = translated[0]
                if val == None:
                    continue
                else:
                    wires[destination] = val
            elif len(translated) == 2:
                [op, val] = translated
                assert "NOT" == op
                if val == None:
                    continue
                else:
                    wires[destination] = ~val
            else:
                assert len(translated) == 3
                a, op, b = translated
                if a == None or b == None:
                    continue
                else:
                    if op == "OR":
                        val = a | b
                    elif op == "AND":
                        val = a & b
                    elif op == "RSHIFT":
                        val = a >> b
                    elif op == "LSHIFT":
                        val = a << b
                    else:
                        assert False
                assert val != None
                wires[destination] = val
            for w, v in wires.items():
                # Convert to unsigned ints.
                wires[w] = v & 0xffff
            print(wires)
            resolved += 1
            parsed[i][1] = True
            print("Resolved: ", i, resolved, len(parsed))

    for p in parsed:
        assert p[1] == True
    return wires['a']

# sample = solve(SAMPLE)
# if sample != SAMPLE_EXPECTED:
#     print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
# assert sample == SAMPLE_EXPECTED
# print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL)
print("SOLUTION: ", solved)
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
