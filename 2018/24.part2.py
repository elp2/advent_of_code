from collections import defaultdict

import re

def return_default():
    return []

REAL=open("24.txt").read()
SAMPLE=open("24.sample.txt").read()

import operator

class Unit:
    def __init__(self, line, team_name, group_num, immune_boost):
        # 18 units each with 729 hit points (weak to fire; immune to cold, slashing)
        #  with an attack that does 8 radiation damage at initiative 10
        self.line = line
        self.team_name = team_name
        self.group_num = group_num
        self.num_units, self.hit_points, self.damage, self.initiative = map(int, list(re.findall(r"(\d+)", line)))
        if team_name == "Immune System":
            self.damage += immune_boost
        split = line.split(" ")
        self.damage_type = split[split.index("damage") - 1]

        elementals = {"weak": set(), "immune": set()}
        if "(" in line:
            estr = line[line.index("(") + 1: line.index(")")]
            estr = estr.replace("to ", "")
            estr = estr.replace(",", "")
            estr = estr.replace(";", "")
            esplit = estr.split(" ")
            for e in esplit:
                if e in elementals:
                    key = e
                else:
                    elementals[key].add(e)
        
        self.weak = elementals["weak"]
        self.immune = elementals["immune"]
        self.init_ep_debug_only = self.effective_power()
    

    def effective_power(self):
        assert self.num_units > 0
        return self.num_units * self.damage


    def attack(self, target):
        assert target.team_name != self.team_name
        if not self.alive():
            return
        dmg = self.damage_to(target)

        before_units = target.num_units
        killed = min(target.num_units, int(dmg / target.hit_points))
        target.num_units -= killed
        # print(self.team_name, " group", self.group_num, "attacks ", "other: ", target.group_num, "dealing: ", dmg, " killing", killed, " isalive: ", target.alive(), "leaving: ", target.num_units, " down from ", before_units)


    def alive(self):
        return self.num_units > 0

    def damage_to(self, target):
        mult = 1
        if self.team_name == target.team_name:
            mult = -1        
        elif self.damage_type in target.weak:
            mult = 2
        elif self.damage_type in target.immune:
            mult = 0
        return mult * self.effective_power()

    def choose_target(self, units, targeted):
        def choose_target_cmp(a, b):
            dta = self.damage_to(a)
            dtb = self.damage_to(b)
            if dta > dtb:
                return -1
            elif dtb > dta:
                return 1
            else:
                if a.effective_power() > b.effective_power():
                    return -1
                elif b.effective_power() > a.effective_power():
                    return 1
                else:
                    if a.initiative > b.initiative:
                        return -1
                    elif b.initiative > a.initiative:
                        return 1
                    else:
                        assert False
        choose_order = sorted(units, key=functools.cmp_to_key(choose_target_cmp))
        damages = []
        for u in choose_order:
            if u.team_name == self.team_name:
                damages.append(-1)
            else:
                dmg_to = self.damage_to(u)
                eligible = not u in targeted.values()
                # print(self.team_name, self.group_num, " could damage ", u.team_name, u.group_num, " for ", dmg_to, "ELIGIBILE: ", eligible)
                if eligible:
                    damages.append(dmg_to)
                else:
                    damages.append(-1)
        
        best = max(damages)
        if best <= 0:
            # print("No best damage:", damages)
            return None
        else:
            target = choose_order[damages.index(best)]
            assert self.team_name != target.team_name
            # print("Chosen -> ", target.group_num)
            return target
    
    def debug(self):
        print(self.team_name, self.num_units)



def parse_lines(raw, boost):
    tstrings = raw.split("\n\n")
    units = []
    for ts in tstrings:
        split = ts.split("\n")
        team_name = split[0].replace(":", "")
        for i in range(1, len(split)):
            line = split[i]
            units.append(Unit(line, team_name, i, boost))
    
    return units

import functools

def group_by_team(units):
    grouped = defaultdict(return_default)
    for u in units:
        grouped[u.team_name].append(u)
        # u.debug()
    return grouped


def target_phase(units):
    targeted = {}
    def target_choosing_cmp(a, b):
        aep = a.effective_power()
        bep = b.effective_power()
        if aep > bep:
            return -1
        elif bep > aep:
            return 1
        else:
            if a.initiative > b.initiative:
                return -1
            elif b.initiative > a.initiative:
                return 1
            else:
                assert False
    
    target_choosing_order = sorted(units, key=functools.cmp_to_key(target_choosing_cmp))
    for u in target_choosing_order:
        chosen = u.choose_target(units, targeted)
        if chosen:
            assert chosen not in targeted.values()
            targeted[u] = chosen

    return targeted

def attack_phase(targeted, units):
    assert targeted
    def attack_cmp(a, b):
        if a.initiative > b.initiative:
            return -1
        else:
            return 1
    attack_order = sorted(units, key=functools.cmp_to_key(attack_cmp))
    for a in attack_order:
        if a in targeted:
            a.attack(targeted[a])


def run_boost(raw, boost):
    units = parse_lines(raw, boost)

    rounds = 0
    while True:
        # print("---------------")
        rounds += 1
        if rounds % 1000 == 0:
            print(boost, rounds)

        # Target Selection Phase.
        units = list(filter(lambda u: u.alive(), units))
        grouped = group_by_team(units)
        if len(grouped) == 1:
            break
        targeted = target_phase(units)
        attack_phase(targeted, units)
    return grouped


def solve(raw):

    boost = 15
    while True:
        try:
            winning = run_boost(raw, boost)
            if "Immune System" in winning:
                ret = 0
                for u in winning["Immune System"]:
                    ret += u.num_units # Doh not number of groups :O
                return ret
            else:
                for u in list(winning.values())[0]:
                    u.debug()
        except AssertionError:
            print("ASSERTIONERROR @ ", boost)
        boost += 1

print("SOLVE: ", solve(REAL)) # NOT 9. Keep getting AssertionErrors afetr boost=16 bc nothing to attack.
