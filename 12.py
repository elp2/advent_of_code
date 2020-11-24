def parse_line(line):
    """0 <-> 454, 528, 621, 1023, 1199"""
    line = line.split(" ")
    return {"id": int(line[0]), 'connected': list(map(lambda num: int(num.replace(",", "")), line[2:]))}

def bfs_programs(lines):
    programs = {}
    for line in lines:
        program = parse_line(line)
        programs[program["id"]] = program
    
    queue = [0]
    seen = []
    while len(queue):
        next = queue.pop()
        if next in seen:
            continue
        seen.append(next)
        queue += programs[next]["connected"]
    return len(seen)

assert 6 == bfs_programs(open('12.sample').readlines())
assert bfs_programs(open('12.txt').readlines()) == 378
