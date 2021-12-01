def solve_part1(a):
    if a == 1:
      # ['seti', '0', '0', '3'] [0, 0, 10551340, 0, 10550400] ip= 35
      c = 10550400
      a = 0
    else:
      c = 940

    a = 0
    b = 0
    d = 0
    e = 0


    d = 1
    while d <= c:
        b = 1
        while c >= b:
            e = d * b
            if e == c:
              a += d
              b += 1
            else:
              b += 1

        # print(a, d)
        d += 1
    return a

def solve_part1_2(a):
    if a == 1:
      # ['seti', '0', '0', '3'] [0, 0, 10551340, 0, 10550400] ip= 35
      a = 0
      b = 0
      c = 10551340
      d = 0
      e = 10550400
    elif a == 0:
        a = 0
        b = 0
        d = 0
        e = 0
        c = 940
    else:
        assert False


    old_a = a

    d = 1
    while c >= d:
        b = 1
        while c >= b:
            if c % d == 0:
                a += d
                break
            break
            
            # e = d * b
            # if e == c:
            #   b += 1
            # else:
            #   b += 1

        if old_a != a:
            print(a, d)
        old_a = a
        d += 1
    return a

def prime_factor_solve(a):
    if a == 1:
        c = 10551340
        a = 0
    else:
        c = 940
    for d in range(1, c+1):
        if c % d == 0:
            a += d
            print(a, d)
    return a


part1 = solve_part1(0)
assert solve_part1_2(0) == part1
assert part1 == 2016 # Solves SUPER fast.
# print(solve_part1(1)) # Still to slow.
assert prime_factor_solve(0) == 2016
print(solve_part1_2(1))
# print(prime_factor_solve(1)) # 39967680 too high # 29417280 too high??? That's the step before.

# a, d
# 15877600 1758400
# 17987680 2110080
# 20625280 2637600
# 24142080 3516800
# 29417280 5275200
# 39967680 10550400
# 39967680
