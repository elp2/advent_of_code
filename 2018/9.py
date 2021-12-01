from collections import defaultdict

class ElpNode:
    def __init__(self, val, n=None, p=None):
        if n:
            n.p = self
            self.n = n
        if p:
            p.n = self
            self.p = p
        self.val = val

def solve(num_players, last_marble):
    scores = [0] * num_players

    zero = ElpNode(0)
    one = ElpNode(1, None, zero)
    two = ElpNode(2, zero, one)    
    current = zero

    player = 0
    for marble_num in range(3, last_marble + 1):
        if marble_num % 10000 == 0:
            print(marble_num)
        player = (player + 1) % num_players

        if marble_num % 23 == 0:
            scores[player] += marble_num

            removed = current.p.p.p.p.p.p.p
            removed.p.n = removed.n
            removed.n.p = removed.p
            current = removed.n
            scores[player] += removed.val
        else:
            new_marble = ElpNode(marble_num, current.n.n, current.n)
            current = new_marble


    return max(scores)

sample = solve(10, 1618)
assert sample == 8317
print("*** SAMPLE PASSED ***")

assert solve(418, 71339) == 412127
print(solve(418, 71339 * 100))
