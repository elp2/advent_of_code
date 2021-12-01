# Generator A starts with 783
# Generator B starts with 325
REAL_START=[783, 325]
SAMPLE_START=[65, 8921]
FACTORS=[16807, 48271]
DIVISOR=2147483647 # 0b1111111111111111111111111111111 2^31

def next_a_value(val, factor):
    while True:
        val = (val * factor) % DIVISOR
        if val & 3 == 0:
            return val


def next_b_value(val, factor):
    while True:
        val = (val * factor) % DIVISOR
        if val & 7 == 0:
            return val


def calc_16_bit_matches(times, start):
    matches = 0
    a, b = start
    for i in range(times):
        a = next_a_value(a, FACTORS[0])
        b = next_b_value(b, FACTORS[1])
        if a & 0b1111111111111111 == b & 0b1111111111111111:
            matches +=1
    return matches

print(calc_16_bit_matches(5_000_000, REAL_START)) # 336


