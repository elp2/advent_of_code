def do_insert(seq, pos, step, insert):
    pos = (pos + step) % len(seq)
    new_seq = seq[:pos + 1] + [insert] + seq[pos + 1:]
    return (pos + 1, new_seq)

def run(step, times):
    insert = 1
    seq = [0]
    pos = 0

    for _ in range(times):
        pos, seq = do_insert(seq, pos, step, insert)
        insert += 1
        # print(pos, seq)
    return seq


def find_after_2017(step):
    seq = run(step, 2017)
    assert len(seq) == 2018
    return seq[seq.index(2017) + 1]

STEP = 343

# assert find_after_2017(3) == 638
# print(find_after_2017(STEP)) # 1914
