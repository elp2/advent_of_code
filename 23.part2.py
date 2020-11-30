# Initial state.
a = 1
b = c = d = e = f = g = h = 0

b = 67
c = b

# if a != 0 goto ANZ # jnz a 2

# When a was 0, this would skip the next 4 lines
# jnz 1 5

# ANZ
b = b * 100 # (6700) # mul b 100 #1

b -= -100000 # sub b -100000 # 2
c = b # set c b # 3
c -= -17000 # sub c -17000 # 4

# b = 106700
# c = 123700

# -23
while True:
    f = 1
    d = 2

    while True:      
        e = 2

        # if (somehow) (d * e == b, then we'll set f=0 and increment h.
        # no need to inc e to figure out.
        if b % d == 0:
            f = 0
        e = b
        # while True:
        #     # this loops until e == b. 
        #     # g = d
        #     # g *= e
        #     # g -= b
        #     if d * e == b:
        #         # jnz g 2
        #         # set f 0 (skipped when g not zero)
        #         f = 0
        #     e += 1 # sub e -1
        #     if e == b:
        #         break
        # jnz g -8

        d += 1 # sub d -1
        g = d # set g d
        g -= b # sub g b
        if d == b:
            break
            # jnz g -13
    if f == 0:
        # jnz f 2
        h -= -1 #sub h -1
    # When b == c this ends
    # g = b # set g b
    # g -= c # sub g c
    if b == c:
        # jnz g 2
        # jnz 1 3 # FINISHES
        print(h) # 905
        assert False
    b -= -17 # sub b -17 --- after 1000 iterations, b == c
    # Always jumps - jnz 1 -23

    # 1000 too high