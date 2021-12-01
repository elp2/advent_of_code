from collections import defaultdict

class Node:
    def __init__(self, line):
        items = line.split(" ")
        self.name = items[0]
        self.weight = int(items[1].replace(")", "").replace("(", ""))
        
        if len(items) > 2:
            self.children = list(map(lambda child: child.strip().replace(",", ""), items[3:]))
            print(self.children)
        else:
            self.children = []
        self.parent = None # Set in next loop.


    def children_weights(self, nodes):
        return list(map(lambda c: nodes[c].subweight(nodes), self.children))


    def subweight(self, nodes):
        children_weights = self.children_weights(nodes)
        return self.weight + sum(children_weights)


    def unweighted_child_index(self, nodes):
        """Returns -1 if nothing unweighted."""
        if len(self.children) == 0:
            return -1
        children_weights = self.children_weights(nodes)
        if sum(children_weights) / 3 == children_weights[0]:
            return -1
        lcw = len(children_weights)
        for i in range(lcw):
            back = (i - 1 + lcw) % lcw
            forwards = (i + 1) % lcw
            if children_weights[back] == children_weights[forwards] and children_weights[back] != children_weights[i]:
                return i


    def balance_fix(self, nodes):
        uci = self.unweighted_child_index(nodes)
        unweighted = nodes[self.children[uci]]
        if unweighted.unweighted_child_index(nodes) == -1:
            # Its subtrees are weighted, return its fixed weight.
            target = nodes[self.children[(uci + 1) % len(self.children)]].subweight(nodes)
            diff = target - unweighted.subweight(nodes)
            return unweighted.weight + diff
        else:
            return unweighted.balance_fix(nodes)

def find_unweighted(filename):
    nodes = {}
    for line in open(filename).readlines():
        node = Node(line)
        nodes[node.name] = node
    for node in nodes.values():
        for child in node.children:
            nodes[child].parent = node.name

    top_node = None
    for node in nodes.values():
        if node.parent == None:
            print(node.name)
            top_node = node
    print(top_node.balance_fix(nodes))


find_unweighted("7.txt") # 362
