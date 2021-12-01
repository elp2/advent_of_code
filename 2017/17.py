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

from collections import defaultdict


def fast_step(step, seq_len, old_to_insert, to_insert, pos):
    pos = (pos + step) % seq_len
    if pos == 0:
        return (pos + 1, to_insert)
    else:
        return (pos + 1, old_to_insert)


def test_fast_step(step):
    insert = 1
    seq = [0]
    pos = 0

    times = 100
    f1 = None
    for _ in range(times):
        fp, f1 = fast_step(step, insert, f1, insert, pos)
        pos, seq = do_insert(seq, pos, step, insert)
        insert += 1
        assert fp == pos
        assert f1 == seq[1]
        # print(pos, seq)
    return seq    

# test_fast_step(STEP)

def part2(step):
    LEN=50_000_000

    fp = 0
    f1 = None
    for seq_len in range(1, LEN + 1):
        if seq_len % 100_000 == 0:
            print(seq_len, fp, f1)
        fp, f1 = fast_step(step, seq_len, f1, seq_len, fp) 
    print(f1)
part2(STEP) # 41797835