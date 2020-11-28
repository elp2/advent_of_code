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


def part1(sequence, steps):
    for step in steps:
        sequence = apply_step(step, sequence)
        print(sequence)
    # print(sequence)
    print("".join(sequence))

part1(["a", "b", "c", "d", "e"], SAMPLE)
part1(list("abcdefghijklmnop"), REAL) # jcobhadfnmpkglie
