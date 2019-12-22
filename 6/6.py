class Orbits:
    def __init__(self, filename):
        self.planets = {}
        self.add_orbits(filename)

    def add_orbits(self, filename):
        lines = open(filename).readlines()
        for line in lines:
            line = line.strip()
            [parent, child] = line.split(')')
            p = self.add_planet(parent)
            c = self.add_planet(child)
            p['children'].append(c)
            c['parent'] = p

    def add_planet(self, planet):
        if planet not in self.planets:
            self.planets[planet] = {'name': planet, 'children': []}
        return self.planets[planet]

    def count_orbits(self):
        return self.count_orbits_recursively(self.planets['COM'], 0)

    def count_orbits_recursively(self, planet, depth):
        child_orbits = 0
        for child in planet['children']:
            child_orbits += self.count_orbits_recursively(child, depth+1)
        return child_orbits + depth

    def san_orbits(self, planet):
        for child in planet['children']:
            if child['name'] == 'SAN':
                return True
        return False

    def distance_to_san(self):
        return self.distance_to_san_recurse(self.planets['YOU'], 0) - 1

    def distance_to_san_recurse(self, planet, distance):
        if 'visited' in planet:
            return -1
        planet['visited'] = True
        if self.san_orbits(planet):
            return distance
        if 'parent' in planet:
            parent_distance = self.distance_to_san_recurse(planet['parent'], distance + 1)
            if parent_distance != -1:
                return parent_distance
        for child in planet['children']:
            child_distance = self.distance_to_san_recurse(child, distance + 1)
            if child_distance != -1:
                return child_distance
        return -1

def test():
    orbits = Orbits('6/sample')
    print(orbits.count_orbits())

# test()

def part1():
    orbits = Orbits('6/input')
    print(orbits.count_orbits())
# part1() # 314702

def part2():
    orbits = Orbits('6/input')
    print(orbits.distance_to_san()) # 440 too high.

part2()