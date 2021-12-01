from collections import defaultdict

def return_default():
    return 0

def dd():
    return defaultdict(return_default)


CHALLENGE_DAY = "9"
REAL = open(CHALLENGE_DAY + ".txt").read()
assert len(REAL) > 1
SAMPLE = open(CHALLENGE_DAY + ".sample.txt").read()
SAMPLE_EXPECTED = 127
# SAMPLE_EXPECTED = 


def parse_lines(raw):
    # Groups.
    # split = raw.split("\n\n")
    # return list(map(lambda group: group.split("\n"), split))

    split = raw.split("\n")

    # return split # raw
    # return list(map(lambda l: l.split(" "), split)) # words.
    return list(map(int, split))
    # return list(map(lambda l: l.strip(), split)) # beware leading / trailing WS

def lastnums(nums, last, sumsto):
    f = last - 25
    to = last
    print("considering ", f, to)
    for j in range(f, to):
        for k in range(f, to):
            if j == k:
                continue
            if nums[j] + nums[k] == sumsto:
                return True
    return False

def pream(nums, last):
    at = last
    for i in range(last, len(nums)):
        print(i)
        if not lastnums(nums, i, nums[i]):
            return nums[i]
        else:
            print("Not", nums[i])



def solve(raw):
    parsed = parse_lines(raw)
    # Debug here to make sure parsing is good.

    TARGET=1639024365
    for i in range(len(parsed)):
        for j in range(i, (len(parsed))):
            arr = parsed[i:j]
            here = sum(arr)
            if here == TARGET:
                return min(arr) + max(arr)


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

# sample = solve(SAMPLE)
# if SAMPLE_EXPECTED is None:
#     print("*** SKIPPING SAMPLE! ***")
# else:
#     assert sample == SAMPLE_EXPECTED
#     print("*** SAMPLE PASSED ***")

solved = solve(REAL)
print("SOLUTION: ", solved)
# assert solved
