from . import utils

SCORE = {
    "C Z": 7,
    "A Z": 8,
    "B Z": 9,
    "A Y": 4,
    "B Y": 5,
    "C Y": 6,
    "A X": 3,
    "B X": 1,
    "C X": 2,
}

def _score_win(opponents:int, mine:int):
    if opponents == mine:
        return 3 # draw
    if mine - opponents == 1: # winning move is exactly 1 step removed
        return 6
    if mine -opponents == -2: # wrap around
        return 6
    return 0


def part2():
    score = 0
    for line in utils.read_inputs(2):
        line = line.strip()
        score += SCORE[line]
    print(score)


if __name__=="__main__":
    part2()
