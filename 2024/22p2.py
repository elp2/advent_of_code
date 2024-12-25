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
SAMPLE_EXPECTED = 23
######################
assert SAMPLE_EXPECTED != None, "Must enter sample value"

def parse_group(group):
    lines = group.split("\n")
    return lines

def parse_lines(raw):
    # Groups.
    # groups = raw.split("\n\n")
    # Do something with the groups.

    return parse_group(raw)

def mix(a, b):
    xored = a ^ b
    return xored

assert mix(42, 15) == 37

def prune(a):
    modded = a % 16777216
    return modded

assert prune(100000000) == 16113920

def step(secret):
    # Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number. 
    # Finally, prune the secret number.
    next = secret * 64
    secret = mix(next, secret)
    secret = prune(secret)

    # Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer.
    # Then, mix this result into the secret number. Finally, prune the secret number.
    next = secret // 32
    secret = mix(next, secret)
    secret = prune(secret)

    # Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret number.
    # Finally, prune the secret number.
    next = secret * 2048
    secret = mix(next, secret)
    secret = prune(secret)
    return secret

assert step(123) == 15887950
expecteds = list(map(int, """15887950
16495136
527345
704524
1553684
12683156
11100544
12249484
7753432
5908254""".split("\n")))
secret = 123
for e in expecteds:
    secret = step(secret)
    assert secret == e

def get_prices_deltas(num, times):
    deltas = []
    secret = num
    prev = secret % 10
    prices = [prev]
    for _ in range(times):
        secret = step(secret)
        price = secret % 10
        prices.append(price)
        deltas.append(price - prev)
        prev = price
    return prices, deltas

p, d = get_prices_deltas(123, 3)
print(p, d)
assert d == [-3, 6, -1]
assert p == [3, 0, 6, 5]

def solve(raw):
    parsed = parse_lines(raw)
    print(parsed)

    ret = 0
    cnt = Counter()
    for line in parsed:
        num = int(line)
        prices, deltas = get_prices_deltas(num, 2000)
        seen_keys = set()
        for start in range(0, len(deltas)):
            end = start + 4
            dkey = deltas[start:end]
            if len(dkey) != 4:
                continue
            dkey = str(dkey)
            if dkey not in seen_keys:
                cnt[dkey] += prices[end]
                seen_keys.add(dkey)

    return cnt.most_common(1)[0][1]

if __name__ == "__main__":
    SAMPLE, REAL = get_raw_inputs(sys.argv)
    SAMPLE = """1
2
3
2024"""

    sample = solve(SAMPLE)
    assert sample == SAMPLE_EXPECTED, "Sample Result %s != %s expected" % (sample, SAMPLE_EXPECTED)
    print("\n*** SAMPLE PASSED ***\n")

    solved = solve(REAL)
    print("SOLUTION: ", solved)
