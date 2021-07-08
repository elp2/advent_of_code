BOARD={}
BOARD[(1, 1)] = 20151125

def prev(pos):
    x, y = pos
    if x == 1:
        return (y - 1, 1)
    else:
        return (x - 1, y + 1)

def value(pos):
    if pos in BOARD:
        return BOARD[pos]
    calc_list = [pos]
    while True:
        p = prev(pos)
        if p in BOARD:
            break
        calc_list.append(p)
        pos = p
    print('Calculated ', len(calc_list))
    while calc_list:
        here = calc_list.pop()
        p = prev(here)
        v = (252533 * BOARD[p]) % 33554393
        BOARD[here] = v
    return BOARD[here]
assert value((1, 1)) == 20151125
assert value((1, 2)) == 31916031
assert value((2, 1)) == 18749137

assert value((6, 4)) == 31527494
print('TESTS PASS')
# row 3010, column 3019.
print("RC", value((3019, 3010))) # 8997277

print(value((3010, 3019)))
