def flip_rotations(f):
    arr = list(map(list, f.split("/")))
    frs = [ "/".join(map(lambda r: "".join(r), arr))]
    # print(arr)

    dim = len(arr[0])
    def mirror_x(pos):
        x, y = pos
        return (dim - 1 - x, y)

    def mirror_y(pos):
        x, y = pos
        return (x, dim - 1 - y)
    
    def rotate(pos):
        x, y = pos
        if dim == 2:
            return {(0, 0): (1, 0), (1, 0): (1, 1), (1, 1): (0, 1), (0, 1): (0, 0)}[(x, y)]
        if dim == 3:
            return {(0, 0): (2, 0), (1, 0): (2, 1), (2, 0): (2, 2), (2, 1): (1, 2), (2, 2): (0, 2), (1, 2): (0, 1), (0, 2): (0, 0), (0, 1): (1, 0), (1, 1): (1, 1)}[(x, y)]

    def apply_transforms(to, transforms):
        dim = len(to[0])
        new = to.copy()
        for trans in transforms:
            new = [[None] * dim for _ in range(dim)]
            for x in range(dim):
                for y in range(dim):
                    nx, ny = trans((x, y))
                    new[ny][nx] = to[y][x]
            to = new
        return "/".join(map(lambda r: "".join(r), new))
    for trans in [[mirror_x], [mirror_y], [mirror_y, mirror_x], [mirror_x, mirror_y], [rotate], [rotate, rotate], [rotate, rotate, rotate]]:
        frs.append(apply_transforms(arr, trans))

    rot4 = apply_transforms(arr, [rotate, rotate, rotate, rotate])
    assert rot4 == frs[0]
    return frs


def parse_patterns(lines):
    patterns = {}
    for line in lines:
        line = line.strip()
        f, to = line.split(" => ")
        fr = flip_rotations(f)
        for frp in fr:
            patterns[frp] = to
    return patterns


# parse_patterns()
REAL = parse_patterns(open("21.txt").readlines())
SAMPLE = parse_patterns(open("21.sample").readlines())

def part1(patterns, iterations = 5):
    arr = [list(".#."), list("..#"), list("###")]
    for iter in range(iterations):
        dim = len(arr[0])
        if len(arr[0]) % 2 == 0:
            step = 2
        elif len(arr[0]) % 3 == 0:
            step = 3
        else:
            assert False
        new_step = step + 1
        new_dim = new_step * int(dim / step)
        new_arr = [[None] * new_dim for _ in range(new_dim)]

        for iy in range(int(dim / step)):
            for ix in range(int(dim / step)):
                key = ""
                for y in range(step):
                    for x in range(step):
                        key += arr[y + iy * step][x + ix * step]
                    if y != step -1:
                        key += "/"
                if key not in patterns:
                    print("Missing ", key)
                    # for pk in patterns.keys():
                    #     if pk.count("#") == key.count("#"):
                    #         print(pk.replace("/", "\n"), "->", key.replace("/", "\n"), "?")
                    # TODO - failing the first board state?
                    assert key in patterns
                else:
                    expanded = patterns[key].split("/")

                assert len(expanded[0]) == step + 1
                for y in range(new_step):
                    for x in range(new_step):
                        new_arr[y + iy * new_step][x + ix * new_step] = expanded[y][x]

        print(new_arr)
        arr_string = "\n".join(map(lambda row: "".join(row), new_arr))
        print(arr_string, arr_string.count("#"))
        arr = new_arr



# part1(SAMPLE, 2)
part1(REAL, 5)