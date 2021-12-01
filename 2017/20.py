def parse_particles(lines):
    particles = []
    for line in lines:
        popen = line.index("<")
        pclose = line.index(">")
        p = line[popen+1:pclose].strip()
        line = line[pclose+1:]
        pos = list(map(int, p.split(",")))


        vopen = line.index("<")
        vclose = line.index(">")
        v = line[vopen+1:vclose].strip()
        line = line[vclose+1:]
        vel = list(map(int, v.split(",")))


        aopen = line.index("<")
        aclose = line.index(">")
        a = line[aopen+1:aclose].strip()
        line = line[aclose+1:]
        acc = list(map(int, a.split(",")))

        # print(p, v, a, pos, vel, acc)
        particles.append((pos, vel, acc))
    return particles

REAL=parse_particles(open("20.txt").readlines())
SAMPLE2=parse_particles(open("20.sample2").readlines())


def move_particle(particle):
    pos, vel, acc = particle
    for i in range(3):
        vel[i] += acc[i]
        pos[i] += vel[i]
    return (particle, (pos[0], pos[1], pos[2]))

def find_closest_long_term(particles):
    print(particles)
    def manhattan_acc(part):
        acc = part[2]
        dist = 0
        for a in acc:
            dist += abs(a)
        return dist


    def manhattan_vel(part):
        acc = part[1]
        dist = 0
        for a in acc:
            dist += abs(a)
        return dist


    def manhattan_pos(part):
        acc = part[0]
        dist = 0
        for a in acc:
            dist += abs(a)
        return dist

    acc_mans = list(map(manhattan_acc, particles))
    min_a = min(acc_mans)
    print(min_a, acc_mans.count(min_a))
    for i in range(len(particles)):
        part = particles[i]
        if manhattan_acc(part) == min_a:
            print(i, part, manhattan_vel(part), manhattan_pos(part))

# find_closest_long_term(REAL) # 161 lowest vel.

from collections import defaultdict

def part2(particles):
    i = 0
    def return_empty():
        return []
    while True:
        i += 1
        if i % 100_000:
            print(len(particles))
        new_particles = []
        seen = defaultdict(return_empty)
        for part in particles:
            new_part, pos = move_particle(part)
            seen[pos].append(new_part)
        for pos, parts in seen.items():
            if len(parts) != 1:
                continue # collision
            new_particles.append(parts[0])
        particles = new_particles

part2(REAL) # 438
