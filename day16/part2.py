from math import floor

# 529100
# 529463 287
# print(len(arr))
# print(650*10_000 - OFFSET, from_start)

def offset():
    num = open('input').readline().strip()
    offset = num[0:7]
    return int(offset)

def build_array(offset, repeats, num):
    partial_repeat = num[offset % len(num):]
    full_repeats = floor((len(num) * repeats - (offset + len(partial_repeat)))/650)
    assert full_repeats * len(num) + offset + len(partial_repeat) == repeats * len(num)

    arr = partial_repeat + num * full_repeats

    return arr

def round(arr):
    i = len(arr) - 1
    prev = 0
    while i >= 0:
        prev += arr[i]
        arr[i] = prev % 10
        i -= 1

def part2(num, repeat, offset, rounds):
    arr = build_array(offset, repeat, num)
    for i in range(0, rounds):
        print(i)
        round(arr)
        # print(arr)
    result = map(lambda x:str(x), arr[0:8])
    print(arr[0:650])
    print(''.join(result))

def string_to_int_list(string):
    return list(map(lambda x: int(x), string))

#part2(string_to_int_list('12345678'), 8, 0, 4)
part2(list(map(lambda x: int(x), open('input').readline().strip())) , 10_000, offset(), 100) # 82994322
# 57996548 too low
    # NUM = list(map(lambda x: int(x), open('input').readline().strip())) 
    # OFFSET = offset()
    # from_start = OFFSET % len(NUM)

