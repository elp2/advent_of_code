def parse_barriers(lines):
    barriers = []
    for line in lines:
        line = line.strip()
        layer, range = line.split(": ")
        range = int(range)
        layer = int(layer)
        while len(barriers) < layer:
            barriers.append(None)
        barriers.append(range)
    return barriers

sample = parse_barriers(open("13.sample").readlines())
print(sample)

def score_barriers(barriers):
    score = 0
    for layer in range(len(barriers)):
        b = barriers[layer]
        if not b:
            continue
        middle = max(b-2, 0)
        end = 1
        cycle = end + middle + end + middle
        bpos = layer % cycle
        if bpos == 0:
            print('Hit at ', layer)
            score += layer * b
    return score

print(score_barriers(sample))

real = parse_barriers(open("13.txt").readlines())
print(score_barriers(real)) # 1588
