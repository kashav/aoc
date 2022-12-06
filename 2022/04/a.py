import sys


def parse():
    ranges = []
    for line in sys.stdin:
        a, b = ([int(x) for x in pair.split("-")] for pair in line.split(","))
        ranges.append((a, b))
    return ranges


def full(a, b):
    return a[0] <= b[0] and b[1] <= a[1]


def partial(a, b):
    return a[1] >= b[0] and a[1] <= b[1]


def part1(data):
    return sum(full(a, b) or full(b, a) for a, b in data)


def part2(data):
    return sum(partial(a, b) or partial(b, a) for a, b in data)


data = parse()
print(part1(data))
print(part2(data))
