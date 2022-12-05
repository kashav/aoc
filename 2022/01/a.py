with open("input", "r+") as input_:
    cals = [0]
    big_n, big_i = -1, -float("inf")
    for line in input_:
        if line == '\n':
            if cals[-1] > big_n:
                big_n = cals[-1]
                big_i = len(cals)
            cals.append(0)
        else:
            cals[-1] += int(line.strip())

# part 1
print(big_n, big_i)

# part 2
top3 = sorted(cals)[-3:]
print(sum(top3))
