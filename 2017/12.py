def parse_line(line):
    """0 <-> 454, 528, 621, 1023, 1199"""
    line = line.split(" ")
    return {"id": int(line[0]), 'connected': list(map(lambda num: int(num.replace(",", "")), line[2:]))}

def bfs_programs(lines):
    programs = {}
    for line in lines:
        program = parse_line(line)
        programs[program["id"]] = program

    groups = 0

    seen = []
    for root in list(programs.keys()):
        if root in seen:
            continue
        groups += 1
        queue = [root]
        while len(queue):
            next = queue.pop()
            if next in seen:
                continue
            seen.append(next)
            queue += programs[next]["connected"]
    return groups

assert 2 == bfs_programs(open('12.sample').readlines())

answer = bfs_programs(open('12.txt').readlines())
print(answer) # 204
