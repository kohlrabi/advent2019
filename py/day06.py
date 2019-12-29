#!/usr/bin/env python3

import fileinput
from collections import defaultdict
from collections import UserDict


class Node:

    def __init__(self, parent=None, children=None):
        self.parent = parent
        if children is not None:
            self.children = children
        else:
            self.children = []


class Nodes(UserDict):

    def add_parent_child(self, parent, child):
        try:
            self[parent].children.append(child)
        except KeyError:
            self[parent] = Node(children=[child])
        try:
            self[child].parent = parent
        except KeyError:
            self[child] = Node(parent=parent)

    def find_root_node(self):
        for k, v in self.items():
            if v.parent is None:
                return k

    def count_children(self, node, depth=1):
        s = len(self[node].children) * depth
        for n in self[node].children:
            s += self.count_children(n, depth+1)
        return s



def part1(nodes):
    root = nodes.find_root_node()
    return nodes.count_children(root, depth=1)


def main():
    nodes = Nodes()

    for line in fileinput.input():
        parent, child = line.rstrip().split(')')
        nodes.add_parent_child(parent, child)

    p1 = part1(nodes)
    print(f'part1: {p1}')

if __name__ == '__main__':
    main()