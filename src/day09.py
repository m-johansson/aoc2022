from . import utils
import math



class PlayingGrid:
    def __init__(self) -> None:
        self.head = (0, 0)
        self.tail = (0, 0)
        self.tail_history = set()
        self.tail_history.add(self.tail)

    def move_head(self, direction: str, moves: int):
        match direction:
            case "R":
                for _ in range(moves):
                    self.head = (self.head[0] + 1, self.head[1])
                    self.move_tail()
            case "L":
                for _ in range(moves):
                    self.head = (self.head[0] - 1, self.head[1])
                    self.move_tail()
            case "U":
                for _ in range(moves):
                    self.head = (self.head[0], self.head[1] + 1)
                    self.move_tail()
            case "D":
                for _ in range(moves):
                    self.head = (self.head[0], self.head[1] - 1)
                    self.move_tail()

    def move_tail(self):
        horz_distance = self.head[0] - self.tail[0]
        vert_distance = self.head[1] - self.tail[1]
        if math.sqrt(math.pow(horz_distance, 2) + math.pow(vert_distance,2)) >= 2:
            new_x = self.tail[0] + math.copysign(1, horz_distance) if abs(horz_distance) >= 1 else self.tail[0]
            new_y = self.tail[1] + math.copysign(1, vert_distance) if abs(vert_distance) >= 1 else self.tail[1]
            self.tail = (new_x, new_y)
        print(f"h:{self.head} t:{self.tail}")
        self.tail_history.add(self.tail)

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
