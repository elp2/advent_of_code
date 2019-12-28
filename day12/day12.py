from collections import defaultdict
from itertools import combinations

class MoonSystem:
    def __init__(self):
        self.moons = []
        # pos = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]
        # pos = [[-8, -10, 0],[5, 5, 10],[2, -7, 3],[9, -8, -3]]
        pos = [[5, -1, 5], [0, -14, 2], [16, 4, 0], [18, 1, 16]]

        for p in pos:
            self.moons.append({'pos': p})
        # self.moons = [{'pos': [5, -1, 5]}, {'pos': [0, -14, 2]}, {'pos': [16, 4, 0]}, {'pos': [18, 1, 1]}]
        # self.moons = [{'pos': [5, -1, 5]}, {'pos': [0, -14, 2]}, {'pos': [16, 4, 0]}, {'pos': [18, 1, 1]}]
        for moon in self.moons:
            moon['vel'] = [0,0,0]

    def step(self):
        self.update_velocities()
        self.update_positions()

    def update_velocities(self):
        for (i,j) in combinations(range(0,4),2):
            m1 = self.moons[i]
            m2 = self.moons[j]
            for axis in range(0, 3):
                m1_val = m1['pos'][axis]
                m2_val = m2['pos'][axis]
                if m1_val != m2_val:
                    if m1_val > m2_val:
                        m1['vel'][axis] -= 1
                        m2['vel'][axis] += 1
                    else:
                        m1['vel'][axis] += 1
                        m2['vel'][axis] -= 1
    
    def update_positions(self):
        for moon in self.moons:
            for axis in range(0,3):
                moon['pos'][axis] += moon['vel'][axis]

    def system_energy(self):
        energy = 0
        for moon in self.moons:
            potential = 0
            kinetic = 0
            for axis in range(0, 3):
                potential += abs(moon['pos'][axis])
                kinetic += abs(moon['vel'][axis])
            energy += potential * kinetic
        return energy

def part1():
    ms = MoonSystem()
    for i in range(0, 1000):
        ms.step()

    print(ms.system_energy()) # 7828.


def part2():
    round = 0
    ms = MoonSystem()

    # Previous states and when we saw them.
    previous_states = [defaultdict(lambda: []), defaultdict(lambda: []), defaultdict(lambda: [])]
    done = [False, False, False]
    while round < 1000000:
        if round % 10000 == 0:
            print(round)
        for axis in range(0, 3):
            if done[axis]:
                continue
            state = (ms.moons[0]['pos'][axis], ms.moons[1]['pos'][axis], ms.moons[2]['pos'][axis], ms.moons[3]['pos'][axis], ms.moons[0]['vel'][axis], ms.moons[1]['vel'][axis], ms.moons[2]['vel'][axis], ms.moons[3]['vel'][axis])
            previous_states[axis][state].append(round)
            if len(previous_states[axis][state]) == 2:
                done[axis] = True
        if done == [True, True, True]:
            break
        ms.step()
        round += 1

    for axis in range(0, 3):
        print(axis)
        for (state, rounds) in previous_states[axis].items():
            if len(rounds) > 1:
                print('[%d] %s -> %s' % (axis, state, rounds))

part2() # 518311327635164 (LCM of the following)
# Periods for each one as follows:
# 0
# [0] (5, 0, 16, 18, 0, 0, 0, 0) -> [0, 186028]
# 1
# [1] (-1, -14, 4, 1, 0, 0, 0, 0) -> [0, 231614]
# 2
# [2] (5, 2, 0, 16, 0, 0, 0, 0) -> [0, 96236]
