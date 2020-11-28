# s1, a spin of size 1: eabcd.
# x3/4, swapping the last two programs: eabdc.
# pe/b

REAL=open('16.txt').readline().strip().split(",")
SAMPLE="s1,x3/4,pe/b".split(",")

def apply_step(step, sequence):
    if step[0] == "s":
        num = int(step[1:])
        recip_num = len(sequence) - num
        return sequence[recip_num:] + sequence[:recip_num]
    elif step[0] == "x":
        other = step[1:]
        posa, posb = other.split("/")
        posa = int(posa)
        posb = int(posb)
        sequence[posa], sequence[posb] = sequence[posb], sequence[posa]
    elif step[0] == "p":
        other = step[1:]
        la, lb = other.split("/")
        posa = sequence.index(la)
        posb = sequence.index(lb)
        sequence[posa], sequence[posb] = sequence[posb], sequence[posa]
    return sequence


def run(sequence, steps):
    for step in steps:
        sequence = apply_step(step, sequence)
    return sequence

# part1(["a", "b", "c", "d", "e"], SAMPLE)
# part1(list("abcdefghijklmnop"), REAL) # jcobhadfnmpkglie

seen = {}

start = "abcdefghijklmnop"
seen[start] = 0
seq = list(start)
# Repeats every 60.
step_num = 1_000_000_000 - (1_000_000_000 % 60)
while True:
    if step_num % 1_000_000_000 == 0:
        print("".join(seq))
        break
    step_num += 1
    seq = run(seq, REAL)
    string = "".join(seq)
    if string in seen:
        print(step_num, "->", seen[string]) # pclhmengojfdkaib




# def part2():
#     start_sequence = list("abcdefghijklmnop")
#     sequence = list("abcdefghijklmnop")
#     steps = REAL
#     for step in steps:
#         sequence = apply_step(step, sequence)
#         print(sequence)