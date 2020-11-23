SEEN = set()

def redistribute_until_seen(memory):
    steps = 0

    def find_maxi(m):
        maxi = 0
        maxm = 0
        for i in range(len(m)):
            if m[i] > maxm:
                maxm = m[i]
                maxi = i
        return maxi
    
    while True:
        maxi = find_maxi(memory)
        maxm = memory[maxi]
        memory[maxi] = 0
        while maxm > 0:
            maxi = (maxi + 1) % len(memory)
            memory[maxi] += 1
            maxm -= 1
        steps += 1
        if str(memory) in SEEN:
            print(memory)
            return steps
        SEEN.add(str(memory))

assert 5 == redistribute_until_seen([0, 2, 7, 0])

memory = list(map(int, open("6.txt").readline().split("\t")))
print(memory)
print(redistribute_until_seen(memory)) # 4074