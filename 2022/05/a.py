import copy
import sys
from collections import deque

"""
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

def parse():
    stks = []
    instrs = []

    read_stks = False

    for line in sys.stdin:
        if not line.strip():
            continue

        if line[1] == '1':
            read_stks = True 
            assert len(stks) == int(line[-3])
            continue

        if read_stks:
            parts = line.split()
            instrs.append([int(parts[x]) for x in (1, 3, 5)])
            continue

        for i in range(0, len(line), 4):
            part = line[i:i+4].strip()
            if len(part) == 0:
                continue
            
            stack_no = i // 4
            while len(stks) <= stack_no:
                stks.append(deque())

            crate = part[1]
            stks[stack_no].appendleft(crate)

    return stks, instrs

def part1(stks, instrs):
    stks = copy.deepcopy(stks)
    for m, f, t in instrs:
        f -= 1
        t -= 1
        for _ in range(m):
            pop = stks[f].pop()
            stks[t].append(pop)
    return ''.join(stk[-1] for stk in stks)

def part2(stks, instrs):
    stks = copy.deepcopy(stks)
    for m, f, t in instrs:
        f -= 1
        t -= 1
        popped = []
        for _ in range(m):
            pop = stks[f].pop()
            popped.append(pop)
        for pop in reversed(popped):
            stks[t].append(pop)
    return ''.join(stk[-1] for stk in stks)

stks, instrs = parse()
print(part1(stks, instrs))
print(part2(stks, instrs))

