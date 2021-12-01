REAL=open("24.txt").readlines()
SAMPLE=open("24.sample").readlines()

def parse_components(lines):
    components = []
    for line in lines:
        split = line.strip().split("/")
        components.append(list(map(int, split)))
    return components

def part1(lines):
    comps = parse_components(lines)
    def best_score(components, match, prev_score):
        best = prev_score
        for i in range(len(components)):
            c = components[i]
            a, b = c
            # assert a != b v
            if a == match or b == match:
                if a == match:
                    to_match = b
                else:
                    to_match = a
                new_comp = components[:i] + components[i + 1:]
                new_score = best_score(new_comp, to_match, prev_score + a + b)
                if new_score > best:
                    best = new_score
        return best
    return best_score(comps, 0, 0)

# samp = part1(SAMPLE)
# assert 31 == samp

# print(part1(REAL)) # 1656

def part2(lines):
    comps = parse_components(lines)
    def best_score(components, match, prev_score, here_len):
        best = prev_score
        best_len = here_len
        for i in range(len(components)):
            c = components[i]
            a, b = c
            # assert a != b v
            if a == match or b == match:
                if a == match:
                    to_match = b
                else:
                    to_match = a
                new_comp = components[:i] + components[i + 1:]
                new_score, new_len = best_score(new_comp, to_match, prev_score + a + b, here_len + 1)
                if new_len > best_len:
                    best = new_score
                    best_len = new_len
                elif new_len == best_len:
                    if new_score > best:
                        best = new_score
        return (best, best_len)
    return best_score(comps, 0, 0, 0)

samp = part2(SAMPLE)
print(samp)
assert 19 == samp[0]

print(part2(REAL)) # 1656 - too high # 1642
