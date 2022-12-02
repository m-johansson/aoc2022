from . import utils

TRANSLATION = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "A": 1,
    "B": 2,
    "C": 3,
}

def _score_win(opponents:int, mine:int):
    if opponents == mine:
        return 3 # draw
    if mine - opponents == 1: # winning move is exactly 1 step removed
        return 6
    if mine -opponents == -2: # wrap around
        return 6
    return 0

def translater(move:str):
    return TRANSLATION[move]

def part1():
    score = 0
    for line in utils.read_inputs(2):
        moves = line.split()
        moves = [translater(move) for move in moves]
        score += _score_win(moves[0], moves[1]) + moves[1]
    print(score)


if __name__=="__main__":
    part1()
