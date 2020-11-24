REAL="225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110"
SAMPLE="3,4,1,5"

EXTRA_LENGTHS=[17, 31, 73, 47, 23]

def apply_hash(lengths, elements, pos=0, skip=0):
    for length in lengths:
        for i in range(int(length / 2)):
            a = (pos + i) % len(elements)
            b = (pos + length - i - 1) % len(elements)
            elements[a], elements[b] = elements[b], elements[a]

        pos += length + skip
        pos = pos % len(elements)
        skip += 1
    return (elements, pos, skip)

e, p, s = apply_hash(list(map(int, SAMPLE.split(','))), list(range(5)))
assert [3, 4, 2, 1, 0] == e
e, p, s = apply_hash(list(map(int, REAL.split(','))), list(range(256))) # 23874
assert e[0] * e[1] == 23874

def calculate_sparse_hash(string):
    lengths = list(map(ord, string)) + EXTRA_LENGTHS
    elements = list(range(256))

    skip = 0
    pos = 0
    for _ in range(64):
        elements, pos, skip = apply_hash(lengths, elements, pos=pos, skip=skip)
    return elements

def calculate_dense_hash(elements):
    dense = ""
    for i in range(0, 255, 16):
        block = elements[i]
        for d in range(15):
            block = block ^ elements[i + 1 + d]
        hexed = hex(block).replace("0x", "")
        if len(hexed) == 1:
            hexed = "0" + hexed
        dense += hexed
    return dense

def knot_hash(string):
    sparse = calculate_sparse_hash(string)
    dense = calculate_dense_hash(sparse)
    assert len(dense) == 32
    return dense

TESTS = [("", "a2582a3a0e66e6e86e3812dcb672a272"), ("AoC 2017", "33efeb34ea91902bb2f59c9920caa6cd"), ("1,2,3", "3efbe78a8d82f29979031a4aa0b16a9d"), ("1,2,4", "63960835bcdc130f0b66d7ff4f6a5a8e")]

for test in TESTS:
    string, expected = test
    knotted = knot_hash(string)
    assert expected == knotted

print(knot_hash(REAL)) # e1a65bfb5a5ce396025fab5528c25a87
