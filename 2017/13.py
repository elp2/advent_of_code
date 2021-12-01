def parse_barriers(lines):
    barriers = []
    for line in lines:
        line = line.strip()
        layer, range = line.split(": ")
        range = int(range)
        layer = int(layer)
        while len(barriers) < layer:
            barriers.append(None)
        middle = max(range - 2, 0)
        end = 1
        range = end + middle + end + middle
        barriers.append(range)
    return barriers

sample = parse_barriers(open("13.sample").readlines())
print(sample)

def score_barriers(barriers, delay=0):
    score = 0
    for layer in range(len(barriers)):
        b = barriers[layer]
        if not b:
            continue
        bpos = (layer + delay) % b
        if bpos == 0:
            return 1 # BROKEN for Part 1.
            # print('Hit at ', layer)
            score += layer * b
    return score

print(score_barriers(sample))

real = parse_barriers(open("13.txt").readlines())

delay = 0
while True:
    delay += 1
    score = score_barriers(real, delay=delay)
    if score == 0:
        print(delay) # 3865118
        break