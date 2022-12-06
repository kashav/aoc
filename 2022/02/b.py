ROCK = 1
PAPER = 2
SCISSORS = 3

LOSS = 0
DRAW = 3
WIN = 6

L = {"A": ROCK, "B": PAPER, "C": SCISSORS, "X": LOSS, "Y": DRAW, "Z": WIN}


def my_move(op, oc):
    if oc == DRAW:
        return op

    if oc == WIN:
        if op == PAPER:
            return SCISSORS
        if op == ROCK:
            return PAPER
        if op == SCISSORS:
            return ROCK

    if op == SCISSORS:
        return PAPER
    if op == PAPER:
        return ROCK
    if op == ROCK:
        return SCISSORS


with open("input", "r+") as fi:
    score = 0

    for line in fi:
        op, outcome = [L[x] for x in line.strip().split()]
        score += outcome + my_move(op, outcome)

    print(score)
