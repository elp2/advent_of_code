REAL="225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110"
SAMPLE="3,4,1,5"

def apply_hash(sequence, num_elements):
    elements = list(range(num_elements))
    lengths = list(map(int, sequence.split(',')))
    skip = 0
    pos = 0
    for length in lengths:
        print(elements)
        for i in range(int(length / 2)):
            a = (pos + i) % len(elements)
            b = (pos + length - i - 1) % len(elements)
            elements[a], elements[b] = elements[b], elements[a]

        pos += length + skip
        pos = pos % len(elements)
        skip += 1
    print(elements)
    print(elements[0] * elements[1])

apply_hash(SAMPLE, 5)
apply_hash(REAL, 256) # 23874
