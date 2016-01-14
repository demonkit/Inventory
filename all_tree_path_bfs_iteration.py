#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
Get all paths from root to the leaves.
"""

import copy


class StackEmpty(Exception):
    pass


class Stack(object):

    def __init__(self):
        self._data = []

    def push(self, obj):
        self._data.append(obj)

    def pop(self):
        try:
            return self._data.pop()
        except IndexError:
            raise StackEmpty

    def empty(self):
        return True if not self._data else False


class Node(object):

    def __init__(self, value):
        self.value = value

        self.__children = []

    def __str__(self):
        # return "<Node %s>" % self.value
        return str(self.value)

    def __repr__(self):
        return self.__str__()

    def append_child(self, node):
        self.__children.append(node)

    @property
    def children(self):
        return self.__children

    @property
    def is_leaf(self):
        return True if not self.__children else False


def traverse_bfs_iterate(root):
    result_paths = []
    node_root_paths = {root: [str(root)]}

    stack = Stack()
    stack.push(root)
    while not stack.empty():
        node = stack.pop()
        path = node_root_paths[node]

        for child in node.children:
            child_path = copy.deepcopy(path)
            child_path.append(str(child))
            node_root_paths[child] = child_path
            if child.is_leaf:
                result_paths.append(child_path)
            else:
                stack.push(child)
    return result_paths


def main():
    """
    Test tree structure is shown in `tree.jpg`.
    """
    root = Node(0)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)

    root.append_child(n1)
    root.append_child(n2)

    n1.append_child(n3)
    n2.append_child(n4)
    n3.append_child(n5)
    n3.append_child(n6)
    n4.append_child(n7)
    n4.append_child(n8)
    n4.append_child(n9)
    print traverse_bfs_iterate(root)


if __name__ == '__main__':
    main()
