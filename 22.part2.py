from collections import defaultdict, deque
import re
import copy

CHALLENGE_DAY = "22"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample2.txt").read()
SAMPLE_EXPECTED = 291
# SAMPLE_EXPECTED = 


def parse_lines(raw):
    # Groups.
    groups = raw.split("\n\n")
    g1 = map(int, groups[0].split("\n")[1:])
    q1 = deque(g1)
    g2 = map(int, groups[1].split("\n")[1:])
    q2 = deque(g2)
    return q1, q2

    # return list(map(lambda group: group.split("\n"), groups))
    
    # lines = raw.split("\n")
    # return lines # raw
    # return list(map(lambda l: l.split(" "), lines)) # words.
    # return list(map(int, lines))
    # return list(map(lambda l: l.strip(), lines)) # beware leading / trailing WS

def play_game(p1, p2, game=0):
    # print("Game ", game)
    seen_states = []

    while p1 and p2:
        # print(p1, p2)
        state = [list(p1), list(p2)]
        if state in seen_states:
            # print("seen", state)
            return p1, 1
        seen_states.append(state)
        
        c1 = p1.popleft()
        c2 = p2.popleft()
        if len(p1) >= c1 and len(p2) >= c2:
            # print("\n\nrecursing", len(p1), c1, len(p2), c2)
            copy1 = deque(list(p1)[:c1])
            copy2 = deque(list(p2)[:c2])
            _, winner = play_game(copy1, copy2, game + 1)
            if winner == 1:
                # print("p1 won", p1)
                p1.append(c1)
                p1.append(c2)
                # print(p1)   
            elif winner == 2:
                # print("p2 won", p2)
                p2.append(c2)
                p2.append(c1)
                # print(p2)
            else:
                assert False
            # print("---back to game ", game, "\n")
        elif c1 > c2:
            # print(c1, c2)
            p1.append(c1)
            p1.append(c2)
        else:
            # print(c1, c2)
            p2.append(c2)
            p2.append(c1)
    if p1:
        # print("Winner was 1", p1)
        return p1, 1
    else:
        # print("Winner was 2", p2)
        return p2, 2


def solve(raw):
    p1, p2 = parse_lines(raw)
    # Debug here to make sure parsing is good.

    winner, wnum = play_game(p1, p2)
    print(winner)

    val = 1
    ret = 0
    while winner:
        ret += val * winner.pop()
        val += 1

    return ret

sample = solve(SAMPLE)
if sample != SAMPLE_EXPECTED:
    print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
assert sample == SAMPLE_EXPECTED
print("\n*** SAMPLE PASSED ***\n")

solved = solve(REAL)
print("SOLUTION: ", solved)
import pandas as pd
df=pd.DataFrame([str(solved)])
df.to_clipboard(index=False,header=False)
print("COPIED TO CLIPBOARD")
