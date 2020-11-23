def diff_checksum(inp):
    checksum = 0
    for row in inp:
        nums = list(map(int, row.split("\t")))
        nums.sort()
        checksum += nums[-1] - nums[0]
    return checksum

# print(diff_checksum(open('2.txt').readlines())) # 51139

def divisor_checksum(inp):
    checksum = 0
    for row in inp:
        nums = list(map(int, row.split("\t")))
        nums.sort()
        nums.reverse()
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] % nums[j] == 0:
                    checksum += int(nums[i] / nums[j])
                    break
    return checksum

print(divisor_checksum(open('2.txt').readlines())) # 272
