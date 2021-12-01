TARGET=3600000 # 36000000/10

def naiive(i):
    useds = []
    here = i
    for j in range(1, int(i / 2) + 1):
        if i % j == 0:
            here += j
            useds.append(j)
    useds.append(i)
    return here, useds

# seens = {}
# for i in range(1, 1024 * 16, 1):
#     h, u = naiive(i)
#     if h not in seens:
#         seens[h] = (i, u)

# ks = sorted(seens.keys())
# for k in ks:
#     v = seens[k]
#     print(k, v)
# 14 = 1 + 2 + 7 + 14 === 24
# 15 = 1 + 3 + 5 + 15 === 24

# Take 1 = 23
# Take 2 = 21
# Take 3 = 18 (wrong), 4 = 14, 5 = 9, 

# 16383 (8192, [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192])
# 36000 (12744, [1, 2, 3, 4, 6, 8, 9, 12, 18, 24, 27, 36, 54, 59, 72, 108, 118, 177, 216, 236, 354, 472, 531, 708, 1062, 1416, 1593, 2124, 3186, 4248, 6372, 12744])


# def first(s):

# TARGET=1000

def first_house():
    max_seen = TARGET - 1
    houses = [0] * TARGET

    for step in range(1, TARGET - 1):
        if step % 1000 == 0:
            print(step)
        for i in range(step, max_seen, step):
            houses[i] += step
            if houses[i] >= TARGET and i < max_seen:
                max_seen = i
                print("new min: ", max_seen, houses[i])
                break
    print(houses[:10])
    return max_seen
# print("Fist house: ", first_house())

# print(naiive(3326400)) # 3326400 too high # 831600

def part2(target):
    max_seen = target - 1
    houses = [0] * target

    for step in range(1, target - 1):
        if step % 1000 == 0:
            print(step)
        deliveries = 0
        for i in range(step, max_seen, step):
            houses[i] += step * 11
            if houses[i] >= target and i < max_seen:
                max_seen = i
                print("new min: ", max_seen, houses[i])
                break
            deliveries += 1
            if deliveries == 50:
                break
    print(houses[:10])
    return max_seen

print("part2: ", part2(36000000)) # 884520
