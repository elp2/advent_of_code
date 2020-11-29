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
SAMPLE=parse_particles(open("20.sample").readlines())


def move_particle(particle):
    pos, vel, acc = particle
    dist = 0
    for i in range(3):
        vel[i] += acc[i]
        pos[i] += vel[i]
        dist += abs(pos[i])
    return (particle, dist)

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

find_closest_long_term(REAL) # 161 lowest vel.

