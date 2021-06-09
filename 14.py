from collections import defaultdict, deque
import re

CHALLENGE_DAY = "14"
REAL = open(CHALLENGE_DAY + ".txt").read()
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
SAMPLE_EXPECTED = 1120

def parse_lines(raw):
    ret = []
    for line in raw.split("\n"):
        # Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds.
        name, _, _, speed, _, _, fly_time, _, _, _, _, _, _, rest_time, _ = line.split(" ")
        ret.append((name, int(speed), int(fly_time), int(rest_time)))
    return ret

def travelled(line, time):
    name, speed, fly_time, rest_time = line
    fly_rest_cycle_time = fly_time + rest_time
    cycles = int(time / fly_rest_cycle_time)
    remain = time - cycles * fly_rest_cycle_time
    return cycles * speed * fly_time + min(remain, fly_time) * speed


def solve(raw, time):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.
    ret = 0
    max_i = -1
    for i, line in enumerate(parsed):
        here = travelled(line, time)
        if here > ret:
            max_i = i
            ret = here

    return ret, max_i

def solve2(raw, time):
    scores = [0] * 20

    for t in range(1, time + 1):
        _, max_i = solve(raw, t)
        print(t, max_i)
        scores[max_i] += 1
    
#    assert sum(scores) == time + 1
    print(scores)
    return max(scores)

sample, _ = solve(SAMPLE, 1000)
if sample != SAMPLE_EXPECTED:
    print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED)
assert sample == SAMPLE_EXPECTED
print("\n*** SAMPLE PASSED ***\n")

solved, _ = solve(REAL, 2503) # 2655
print("SOLUTION: ", solved)

# SAMPLE_EXPECTED2 = 689
# sample = solve2(SAMPLE, 1000)
# if sample != SAMPLE_EXPECTED2:
#     print("SAMPLE FAILED: ", sample, " != ", SAMPLE_EXPECTED2)
# assert sample == SAMPLE_EXPECTED2
# print("\n*** SAMPLE PASSED ***\n")

solved = solve2(REAL, 2503) # 1059
print("SOLUTION: ", solved)

