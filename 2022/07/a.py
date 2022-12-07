import sys
from collections import deque


class Node:
    def __init__(self, parent, name):
        self._name = name
        self._parent = parent

    def size(self):
        raise NotImplementedError


class Directory(Node):
    def __init__(self, parent, name):
        super().__init__(parent, name)
        self.children = {}

    def add_child(self, node):
        self.children[node._name] = node

    def size(self):
        return sum(c.size() for c in self.children.values())

    def print_tree(self, depth=0):
        spaces = " " * depth
        print(f"{spaces}- {self._name} (dir, size={self.size()})")
        for child in self.children.values():
            child.print_tree(depth + 2)


class File(Node):
    def __init__(self, parent, name, size):
        super().__init__(parent, name)
        self._size = size

    def size(self):
        return self._size

    def print_tree(self, depth):
        spaces = " " * depth
        print(f"{spaces}- {self._name} (file, size={self.size()})")


def build_tree():
    root: Node = None
    cwd: Node = None
    in_ls = False

    for line in sys.stdin:
        line = line.strip()

        if line[0] == "$":
            in_ls = False

            if line[2:4] == "cd":
                dirname = line[5:]

                if dirname == "..":
                    cwd = cwd._parent
                else:
                    node = Directory(cwd, dirname)
                    if dirname == "/":
                        root = node
                    else:
                        cwd.add_child(node)
                    cwd = node
            else:
                assert line[2:4] == "ls"
                in_ls = True

            continue

        if in_ls:
            if line[:3] == "dir":
                dirname = line[4:]
                cwd.add_child(Directory(cwd, dirname))
            else:
                size, fname = line.split()
                cwd.add_child(File(cwd, fname, int(size)))

    return root


def part1(root):
    total = 0

    q = deque([root])
    while q:
        node = q.popleft()
        if type(node).__name__ == "Directory":
            size = node.size()
            if size <= 100000:
                total += size
            q.extend(node.children.values())

    return total


SYSTEM_SIZE = 70000000
REQUIRED_FREE = 30000000


def part2(root):
    free = SYSTEM_SIZE - root.size()
    to_delete = REQUIRED_FREE - free

    sizes = []
    q = deque([root])
    while q:
        node = q.popleft()
        if type(node).__name__ == "Directory":
            size = node.size()
            sizes.append((size, node._name))
            q.extend(node.children.values())

    for s, n in sorted(sizes):
        if s > to_delete:
            return n, s

    assert False


root = build_tree()
# root.print_tree()
print(part1(root))
print(part2(root))
