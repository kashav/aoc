import sys


def parse_input():
    grid = []
    for line in sys.stdin:
        grid.append([int(x) for x in line.strip()])
    return grid


def part1(grid):
    def top(i, j):
        for k in range(i - 1, -1, -1):
            if grid[k][j] >= grid[i][j]:
                return False
        return True

    def left(i, j):
        for k in range(j - 1, -1, -1):
            if grid[i][k] >= grid[i][j]:
                return False
        return True

    def right(i, j):
        for k in range(j + 1, len(grid[i])):
            if grid[i][k] >= grid[i][j]:
                return False
        return True

    def bottom(i, j):
        for k in range(i + 1, len(grid)):
            if grid[k][j] >= grid[i][j]:
                return False
        return True

    def is_visible(i, j):
        return top(i, j) or left(i, j) or right(i, j) or bottom(i, j)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            count += is_visible(i, j)
    return count


def part2(grid):
    def top(i, j):
        for k in range(i - 1, -1, -1):
            if grid[k][j] >= grid[i][j]:
                return i - k
        return i

    def left(i, j):
        for k in range(j - 1, -1, -1):
            if grid[i][k] >= grid[i][j]:
                return j - k
        return j

    def right(i, j):
        for k in range(j + 1, len(grid[i])):
            if grid[i][k] >= grid[i][j]:
                return k - j
        return len(grid[i]) - (j + 1)

    def bottom(i, j):
        for k in range(i + 1, len(grid)):
            if grid[k][j] >= grid[i][j]:
                return k - i
        return len(grid) - (i + 1)

    def score(i, j):
        return top(i, j) * bottom(i, j) * left(i, j) * right(i, j)

    highest = -float("inf")
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            highest = max(highest, score(i, j))
    return highest


grid = parse_input()
print(part1(grid))
print(part2(grid))
