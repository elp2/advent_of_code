# -----
#     0     0     0     0     0     0     0     0     0     0     0
#     0     0     0     0   943  5678   948     0     0     0     0
#     0     0     0   943  6611  7457  6587   948     0     0     0
#     0     0   943  6611  7457  7520  7457  6587   948     0     0
#     0   943  6611  7457  7520  7457  7520  7457  6587   948     0
#     0  5678  7457  7520  7457  7520  7457  7520  7457  5674     0
#     0   950  6587  7457  7520  7457  7520  7457  6607   965     0
#     0     0   950  6587  7457  7520  7457  6607   965     0     0
#     0     0     0   950  6587  7457  6607   965     0     0     0
#     0     0     0     0   950  5674   965     0     0     0     0
#     0     0     0     0     0     0     0     0     0     0     0
# -----

e = 26501365 // 131
assert e * 131 + 65 == 26501365

def solve_fast(e):
    ret = 0
    center = 7520
    centera = 7457
    ret += e * centera + (e-1) * center
    for ex in range(1, e):
        ret += 2 * (ex * centera + (ex - 1) * center)

    edgetopleft = 5678 * 2
    edgebotright = 5674 * 2
    ret += edgetopleft + edgebotright

    botleftint = 6587 * (e - 1)
    topleftint = 6611 * (e - 1)
    toprightint = 6587 * (e - 1)
    botrightint = 6607 * (e - 1)
    ret += botleftint + topleftint + toprightint + botrightint

    # all of these are e times
    botleft = 950 * e
    botright = 965 * e
    topright = 948 * e
    topleft = 943 * e
    ret += botleft + botright + topright + topleft
    return ret

print(solve_fast(4))
assert solve_fast(4) == 304096
print(solve_fast(6))
assert solve_fast(6) == 633952
print(solve_fast(e))
