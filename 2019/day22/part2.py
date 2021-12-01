# Massive shout out to https://codeforces.com/blog/entry/72593 and https://codeforces.com/blog/entry/72527.

NUM_CARDS = 119315717514047
NUM_SHUFFLES = 101741582076661

def compose_functions(a, b, c, d):
    """If f(x) = ax + b mod m, and g(x) = cx + d mod m, returns y and z in yx + z mod m. for g(f(x))."""
    return (a * c, b * c + d)

def a_b_for_line(line):
    words = line.strip().split(' ')
    if words[0] == 'cut':
        return (1, -int(words[1]))
    elif words[1] == 'into':
        return (-1, -1)
    else:
        return (int(words[3]), 0)

def shuffle_function(lines):
    composed = None
    for line in lines:
        (c, d) = a_b_for_line(line)
        if composed:
            composed = compose_functions(composed[0], composed[1], c, d)
        else:
            composed = (c, d)
        # print(composed)
    return composed

forwards_shuffle = shuffle_function(open('input').readlines())

def apply_forwards(x, m):
    """X ends up where after 1 shuffle round."""
    (a, b) = shuffle_function(open('input').readlines())
    return (a * x + b) % m

def apply_backwards(x, m):
    """What ends up at x after 1 shuffle round."""
    (a, b) = shuffle_function(open('input').readlines())
    return ((x-b) * multiplicative_inverse(a, m)) % m

def multiplicative_inverse(a, m):
    return exponentation_by_squaring(a, m-2, m)

def apply_forwards_n(x, m, k):
    (a, b) = shuffle_function(open('input').readlines())
    A = exponentation_by_squaring(a, k, m)
    B = geometric_sum(b, a, k, m)
    return (A * x + B) % m

def apply_backwards_n(x, m, k):
    # F-k(x) = (x - B*(a^i-k + a^i-k+ 1...)) / a^k mod m.
    # I expanded this one myself.
    (a, b) = shuffle_function(open('input').readlines())
    return ((x - geometric_sum(b, a, k, m)) * multiplicative_inverse(exponentation_by_squaring(a, k, m), m)) % m

def geometric_sum(a, r, n, m):
    numerator = a * (1 - exponentation_by_squaring(r, n, m))
    return (numerator * multiplicative_inverse(1 - r, m)) % m

def exponentation_by_squaring(x, n, m):
    if n == 0:
        # Normal rules apply.
        return 1
    if n % 2 == 0:
        x_exp_n2 = exponentation_by_squaring(x, n/2, m)
        return (x_exp_n2 * x_exp_n2) % m
    else:
        squarable_near_n2 = exponentation_by_squaring(x, (n-1) / 2, m)
        return (squarable_near_n2 * squarable_near_n2 * x) % m

# Last time.
NUM_PART1_CARDS = 10007
PART1_START = 2019
forward = apply_forwards(PART1_START, NUM_PART1_CARDS)
assert forward == 8502

backward = apply_backwards(forward, NUM_PART1_CARDS)
assert backward == PART1_START

forward_1 = apply_forwards_n(PART1_START, NUM_PART1_CARDS, 1)
assert forward_1 == forward

backward_1 = apply_backwards_n(forward_1, NUM_PART1_CARDS, 1)
assert backward_1 == backward

PART2_START = 2020
back_big = apply_backwards_n(PART2_START, NUM_CARDS, NUM_SHUFFLES)
print(back_big) # 41685581334351
forwards_back_big = apply_forwards_n(back_big, NUM_CARDS, NUM_SHUFFLES)
assert forwards_back_big == PART2_START