from collections import defaultdict

INPUT=open("11.txt").readline().strip()
STEPS=INPUT.strip().split(",")

OPPOSITES={'n': 's', 's': 'n', 'ne': 'sw', 'sw': 'ne', 'nw': 'se', 'se': 'nw'}
SUMS={('n', 'se'): 'ne', ('n', 'sw'): 'nw', ('s', 'nw'): 'sw', ('s', 'ne'): 'se'}

def add_dirs(a, b):
    if OPPOSITES[a] == b or a == b:
        return []
    if len(a) == 1:
        key = (a, b)
    else:
        key = (b, a)
    if key in SUMS:
        return [SUMS[key]]
    return [a, b]


def collapse_steps(steps):
    def ret_zero(): return 0
    collapsed = defaultdict(ret_zero)
    for step in steps:
        opp = OPPOSITES[step]
        if collapsed[opp] > 0:
            collapsed[opp] -=1
        else:
            collapsed[step] += 1

    for key in list(collapsed.keys()):
        if collapsed[key] == 0:
            del collapsed[key]
    return collapsed

def add_steps(collapsed):
    for ns in ['n', 's']:
        for key in list(collapsed.keys()):
            if key == ns:
                continue
            added = add_dirs(ns, key)
            if len(added) == 1:
                amt = min(collapsed[key], collapsed[ns])
                collapsed[key] -= amt
                collapsed[ns] -= amt
                collapsed[added[0]] += amt
    return collapsed

def distance(steps):
    collapsed = collapse_steps(steps)
    added = add_steps(collapsed)
    return sum(added.values())


assert distance(STEPS) == 812 # 812

max_dist = 0
for i in range(len(STEPS)):
    max_dist = max(max_dist, distance(STEPS[:i+1]))
print(max_dist) # 1603
