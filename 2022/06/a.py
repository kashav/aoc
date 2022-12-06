import sys

def unique_window(buf, N):
    start = 0

    while len(set(data[start:start+N])) != N:
        start += 1

    return start + N

data = sys.stdin.readline().strip()
print(unique_window(data, 4)) # 1
print(unique_window(data, 14)) # 2 

