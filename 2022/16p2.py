from collections import defaultdict, deque, Counter
from itertools import combinations, combinations_with_replacement, permutations
from functools import reduce
import math
import numpy as np
from operator import add, mul, itemgetter, attrgetter
import re
import functools
import multiprocessing

DS = [[-1, 0], [1, 0], [0, 1], [0, -1]]
DS8 = DS + [[-1, -1], [1, -1], [-1, 1], [1, 1]]
def arounds_inside(x, y, diagonals, w, h):
    ret = []
    for dx, dy in DS8 if diagonals else DS:
        ret.append((x + dx, y + dy))


# GPT-Chat couldn't write this so I have to :(
def divide_array(array, min_size):
    seens = set()
    ret = []
    counter = 0
    while True:
        binary = format(counter, 'b')
        counter += 1

        binary = binary + "0" * (len(array) - len(binary))
        if len(binary) > len(array):
            break
        a = []
        b = []
        for i, c in enumerate(binary):
            if c == "1":
                a.append(array[i])
            else:
                b.append(array[i])
        b += array[i + 1:]
        if tuple(a) in seens or tuple(b) in seens:
            continue
        if len(a) < min_size or len(b) < min_size:
            continue
        seens.add(tuple(a))
        seens.add(tuple(b))
        ret.append((a, b))
    return ret


CHALLENGE_DAY = "16"
REAL = open(CHALLENGE_DAY + ".txt").read()

SAMPLE_EXPECTED = 1707
if SAMPLE_EXPECTED:
    SAMPLE = open(CHALLENGE_DAY + ".s.txt").read()


def parse_lines(raw):
    lines = raw.split("\n")

    ret = []
    order_mapping = {}
    for i in range(len(lines)):
        name = lines[i].split(" ")[1]
        order_mapping[name] = i
    # Valve AW has flow rate=0; tunnels lead to valves DS, AA
    for l in lines:
        # Valve AW has flow rate=0; tunnels lead to valves DS, AA
        l = l.replace(";", "")
        l = l.replace(",", "")
        l = l.replace("=", " ")

        ls = l.split(" ")
        f = ls[1]
        rate = int(ls[5])
        dests = list(map(lambda d: order_mapping[d], ls[10:]))
        ret.append((f, rate, dests))

    distances = {}
    for i in range(len(lines)):
        q = deque()
        q.append((i, 0))
        idists = {}
        while len(q):
            at, dist = q.popleft()
            if at in idists:
                continue
            idists[at] = dist
            for n in ret[at][2]:
                q.append((n, dist + 1))
        distances[i] = idists

    return ret, distances, order_mapping["AA"]

MAX_SECONDS = 26

def max_score(pair, flows, start_index, distances):
    a, b = pair
    a_flow = solve_int(flows, start_index, a, distances)
    b_flow = solve_int(flows, start_index, b, distances)
    print(a_flow, b_flow,  a_flow + b_flow)

    return a_flow + b_flow

def solve(raw, min_size):
    pipes, distances, start_index = parse_lines(raw)
    flows = list(map(lambda p: p[1], pipes))

    openable_is = [i for i in range(len(flows)) if flows[i] > 0]

    divided = divide_array(openable_is, min_size)

    partial_func = functools.partial(max_score, flows=flows, start_index=start_index, distances=distances)

    max_flow = 0
    chunki = 0
    CHUNK_SIZE = 8 * 8
    while chunki < len(divided):
        chunk = divided[chunki:chunki + CHUNK_SIZE]
        with multiprocessing.Pool() as pool:
            # Use the map method to apply the function to each item in the list
            results = pool.map(partial_func, chunk)
            max_flow = max(max(results), max_flow)

            print("@", chunki, float(chunki) / len(divided), max_flow)
            chunki += CHUNK_SIZE

    print(max_flow)
    return max_flow

def solve_int(flows, start_index, visits, distances):
    best = 0
    for ordering in permutations(visits):
        secs = 0
        flow = 0
        at = start_index
        for p in ordering:
            dist = distances[at][p]
            secs += dist + 1
            if secs >= MAX_SECONDS:
                break
            flow += (MAX_SECONDS - secs) * flows[p]
            at = p
        best = max(best, flow)

    return best
if __name__ == "__main__":
    if SAMPLE_EXPECTED != None:
        sample = solve(SAMPLE, 0)
        if sample != SAMPLE_EXPECTED:
            print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
        assert sample == SAMPLE_EXPECTED
        print("\n*** SAMPLE PASSED ***\n")
    else:
        print("Skipping sample")

    solved = solve(REAL, 5)
    assert solved != 1457
    print("SOLUTION: ", solved)
