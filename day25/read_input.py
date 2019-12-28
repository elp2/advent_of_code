# Read input to see if I can get hints about the solution.

memory = list(map(lambda x: int(x), open('input').readline().split(',')))
memory_ascii = ''.join(list(map(lambda x: chr(x) if x >= 0 and x <255 else '?', memory)))
# Result: It's encoded.
# See if it's a simple ROT-x encryption.

def find_deltas(chars):
    deltas = []
    last = None
    for char in chars:
        if last:
            deltas.append(ord(char) - ord(last))
        last = char
    return deltas

known = 'You got in through a hole in the floor here.'
known_deltas = find_deltas(known)
memory_deltas = find_deltas(memory_ascii)

offset = 0
while offset < len(memory_ascii):
    memory_segment = memory_deltas[offset:offset + len(known_deltas)]
    if memory_segment == known_deltas:
        print(offset)
    offset += 1

# Not a simple offset.