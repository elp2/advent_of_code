class Node:
    def __init__(self, line):
        items = line.split(" ")
        self.name = items[0]
        # 1
        if len(items) > 2:
            self.children = list(map(lambda child: child.strip().replace(",", ""), items[3:]))
            print(self.children)
        else:
            self.children = []
        self.parent = None # Set in next loop.

def find_parent(filename):
    nodes = {}
    for line in open(filename).readlines():
        node = Node(line)
        nodes[node.name] = node
    for node in nodes.values():
        for child in node.children:
            nodes[child].parent = node.name

    for node in nodes.values():
        if node.parent == None:
            print(node.name)

find_parent("7.txt") # vvsvez
