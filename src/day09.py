from . import utils
import math

DIRECTIONS = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


class PlayingGrid:
    def __init__(self) -> None:
        self.knots = [(0, 0) for _ in range(10)]
        self.tail_history = set()
        self.tail_history.add(self.knots[-1])

    def move_knot(self, knot_index, movement):
        new_cords = []
        for i in range(2):
            old = self.knots[knot_index][i]
            diff = movement[i]
            new_cords.append(old + diff)
        self.knots[knot_index] = tuple(new_cords)

    def propagate_movement(self, knot_index):
        puller = self.knots[knot_index - 1]
        mover = self.knots[knot_index]
        horz_distance = puller[0] - mover[0]
        vert_distance = puller[1] - mover[1]
        if math.sqrt(math.pow(horz_distance, 2) + math.pow(vert_distance, 2)) >= 2:
            move_x = math.copysign(1, horz_distance) if abs(horz_distance) >= 1 else 0
            move_y = math.copysign(1, vert_distance) if abs(vert_distance) >= 1 else 0
            self.move_knot(knot_index, (move_x, move_y))

    def cascade(self, movement):
        self.move_knot(0, movement)
        for i in range(1, len(self.knots)):
            self.propagate_movement(i)
        self.tail_history.add(self.knots[-1])

    def move_head(self, direction: str, moves: int):
        movement = DIRECTIONS[direction]
        for _ in range(moves):
            self.cascade(movement)

    def get_answer(self):
        return len(self.tail_history)


if __name__ == "__main__":
    pg = PlayingGrid()
    lines = utils.read_inputs(9)
    for l in lines:
        temp = l.split()
        direction = temp[0]
        moves = int(temp[1])
        pg.move_head(direction, moves)
    print(pg.get_answer())
