from collections import defaultdict, deque
import re
from itertools import combinations

def parse_line(line):
    ret = []
    for x in line:
        if not x:
            continue
        if x[0] in "0123456789":
            ret.append(int(x))
        else:
            ret.append(x)
    return ret

WEAPONS = list(map(lambda r: r.split(" "), """Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0""".split("\n")))
WEAPONS = [parse_line(r) for r in WEAPONS]

ARMOR = list(map(lambda r: r.split(" "), """Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5""".split("\n")))
ARMOR = [parse_line(r) for r in ARMOR]


RINGS = list(map(lambda r: r.split(" "), """Damage+1    25     1       0
Damage+2    50     2       0
Damage+3   100     3       0
Defense+1   20     0       1
Defense+2   40     0       2
Defense+3   80     0       3""".split("\n")))
RINGS = [parse_line(r) for r in RINGS]

def battle(weapon_index, armor_index, ring_indexes, boss_hp, boss_damage, boss_armor):
    assert len(ring_indexes) <= 2

    cost = 0
    hp = 100
    dmg = 0
    arm = 0

    _, c, d, a = WEAPONS[weapon_index]
    cost += c
    dmg += d
    arm += a

    if armor_index != 0:
        _, c, d, a = ARMOR[armor_index - 1]
        cost += c
        dmg += d
        arm += a

    for ri in ring_indexes:
        _, c, d, a = RINGS[ri]
        cost += c
        dmg += d
        arm += a

    print("START: ", cost, dmg, arm)
    while True:
        boss_hp -= max(0, dmg - boss_armor)
        if hp <= 0 or boss_hp <= 0:
            break

        hp -= max(0, boss_damage - arm)
        if hp <= 0 or boss_hp <= 0:
            break
        print("\t" + str(hp) + "\t" +str(boss_hp))

    if hp > 0:
        print("WIN", cost, hp, boss_hp)
        assert boss_hp <= 0
        return cost
    else:
        print("LOSE", cost, hp, boss_hp)

        return 1000000000


def solve():
    ret = 1000000000

    bhp = 109
    bd = 8
    ba = 2
    for weapon_index in range(len(WEAPONS)):
        for armor_index in range(len(ARMOR) + 1):
            ris = list(range(len(RINGS)))
            rings = [[]]
            for ri in ris:
                rings.append([ri])
            for rc in combinations(ris, 2):
                rings.append(rc)

            for r in rings:
                ret = min(ret, battle(weapon_index, armor_index, r, bhp, bd, ba))
            print(ret)
    return ret

solved = solve()
print("SOLUTION: ", solved) # 111
