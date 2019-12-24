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

ms = MoonSystem()
for i in range(0, 1000):
    ms.step()

print(ms.system_energy()) # 7828.
            
