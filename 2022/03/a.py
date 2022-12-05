def score(l):
    r = ord(l) - ord('a') + 1
    if r < 0:
        r += 58
    return r

def part1():
    with open("input", "r+") as fi:
        total = 0
        for line in fi:
            line = line.strip()
            n = len(line) // 2
            a, b = [set(x) for x in (line[:n], line[n:])]
            c = a.intersection(b)
            assert len(c) == 1
            total += score(c.pop())
        print(total)

def part2():
    with open("input", "r+") as fi:
        total = 0
        lines = fi.readlines()
        for i in range(0, len(lines), 3):
            group = map(lambda l: set(l.strip()), lines[i:i+3])
            common = set.intersection(*group)
            assert len(common) == 1
            total += score(common.pop())
    print(total)

part1()
part2()
