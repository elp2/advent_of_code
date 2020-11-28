# Generator A starts with 783
# Generator B starts with 325
REAL_START=[783, 325]
SAMPLE_START=[65, 8921]
FACTORS=[16807, 48271]
DIVISOR=2147483647 # 0b1111111111111111111111111111111 2^31

def next_value(val, factor):
    return (val * factor) % DIVISOR


def calc_16_bit_matches(times, start):
    matches = 0
    a, b = start
    for i in range(times):
        a = next_value(a, FACTORS[0])
        b = next_value(b, FACTORS[1])
        if a % 65536 == b % 65536:
            matches +=1
    return matches

print(calc_16_bit_matches(40_000_000, REAL_START)) # 650


