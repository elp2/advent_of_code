class ElpNode:
    def __init__(self, val, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        if self.prev:
            self.prev.nxt = self
        self.nxt = nxt
        if self.nxt:
            self.nxt.prev = self



REAL = "467528193"
SAMPLE = "389125467"
# SAMPLE_EXPECTED = None
SAMPLE_EXPECTED = "67384529"


def get_cups(cups_str, num_cups):
    cups = list(cups_str)
    cups = list(map(int, cups))
    i = 0

    list_nodes = {}
    prev = None
    start = None
    for i, num in enumerate(cups):
        list_nodes[num] = ElpNode(num, prev=prev)
        prev = list_nodes[num]
        if start == None:
            start = prev

    for num in range(10, num_cups + 1):
        list_nodes[num] = ElpNode(num, prev=prev)
        prev = list_nodes[num]
  
    print("MAX: ", i)
    
    prev.nxt = list_nodes[start.val]
    start.prev = prev

    assert len(list_nodes) == num_cups
    verify_nodes(list_nodes)
    return list_nodes

def verify_nodes(nodes):
    lefts = set()
    rights = set()
    for i in range(1, len(nodes) + 1):
        node = nodes[i]
        left = node.prev
        lefts.add(left.val)
        right = node.nxt
        rights.add(right.val)
        assert left != None
        assert right != None
    assert len(lefts) == len(nodes)
    assert len(rights) == len(nodes)


def print_nodes(nodes, current_node):
    line = ""
    node = current_node
    for _ in range(len(nodes)):
        vstr = str(node.val)
        if node == current_node:
            line += " (" + vstr + ")"
        else:
            line += " " + vstr
        node = node.nxt
    print(line)

def run_moves(cups_str, num_moves, num_cups):
    list_nodes = get_cups(cups_str, num_cups)

    current_node = list_nodes[int(cups_str[0])]
    for move in range(num_moves):
        # print_nodes(list_nodes, current_node)
        if move % 100000 == 0:
            # verify_nodes(list_nodes)
            print(move, "VERIFIED!")

        a = current_node.nxt
        b = a.nxt
        c = b.nxt
        current_node.nxt = c.nxt
        current_node.nxt.prev = current_node

        destination = current_node.val - 1 

        invalid_dests = [a.val, b.val, c.val]
        while True:
            if destination in invalid_dests:
                destination -= 1
            elif destination <= 0:
                destination = num_cups
            else:
                break
        # print("Destination: ", destination)
        destination_node = list_nodes[destination]
        dnext = destination_node.nxt
        destination_node.nxt = a
        a.prev = destination_node
        dnext.prev = c
        c.nxt = dnext
        current_node = current_node.nxt

    return list_nodes

def part1(num_moves):
    nodes = run_moves("389125467", num_moves, 9)
    print("PRINTED: ")
    print_nodes(nodes, nodes[1])
    node = nodes[1].nxt

    ret = ""
    while node.val != 1:
        ret += str(node.val)
        node = node.nxt
    
    return ret


def part2(cups):
    nodes = run_moves(cups, 10_000_000, 1_000_000)
    print("PRINTED: ")
    one = nodes[1]

    return one.nxt.val * one.nxt.nxt.val


# assert part1(10) == "92658374"
# assert part1(100) == "67384529"

# assert part2("389125467") == 149245887792
print("P2: ", part2("467528193"))