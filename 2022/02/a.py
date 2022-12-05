ROCK = 1
PAPER = 2
SCISSORS = 3

LOSS = 0
DRAW = 3
WIN = 6

def is_win(a, b):
    if a == ROCK and b == PAPER:
        return True

    if a == PAPER and b == SCISSORS:
        return True

    if a == SCISSORS and b == ROCK:
        return True

    return False

L = {
        "A": ROCK,
        "B": PAPER,
        "C": SCISSORS,
        "X": ROCK,
        "Y": PAPER,
        "Z": SCISSORS
}

with open("input", "r+") as fi:
    score = 0

    for line in fi:
        op, me = [L[x] for x in line.strip().split()]

        if op == me:
            score += DRAW
        elif is_win(op, me):
            score += WIN
        else:
            score += LOSS

        score += me

    print(score)
