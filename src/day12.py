from . import utils


class HeightMap:
    def __init__(self) -> None:
        self.heights = {}

    def set_height(self, x: int, y: int, h: int):
        self.heights[(x, y)] = h


def height_translator(char):
    specials = {
        "S": ord("a"),
        "E": ord("z"),
    }
    if char in specials:
        return specials[char] - ord("a")
    return ord(char) - ord("a")


class Positions:
    def __init__(self, x: int, y: int, hm: HeightMap) -> None:
        self.positions = set([(x, y)])
        self.old_positions = set()
        self.steps = 0
        self.hm = hm

    def remember(self):
        self.old_positions.update(self.positions)

    @staticmethod
    def get_neighbors(pos):
        x = pos[0]
        y = pos[1]
        return ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))

    def seek(self, target, max_steps=1e3):
        while True:
            print(self.steps)
            if target in self.positions:
                return self.steps
            if self.steps >= max_steps:
                return max_steps
            self.remember()
            self.steps += 1
            new_positions = set()
            for pos in self.positions:
                height = self.hm.heights[pos]
                neighbors = self.get_neighbors(pos)
                possible = (
                    k
                    for k in neighbors
                    if k not in self.old_positions
                    and self.hm.heights.get(k, 100) <= height + 1
                )
                new_positions.update(possible)
            self.positions = new_positions


def main(lines):
    hm = HeightMap()
    starts = []
    for y, l in enumerate(lines):
        for x, char in enumerate(l):
            if char == "S" or char == "a":
                starts.append((x, y))
            elif char == "E":
                target = (x, y)
            hm.set_height(x, y, height_translator(char))
    steps = []
    for position in starts:
        place = Positions(position[0], position[1], hm)
        if steps:
            steps.append(place.seek(target, max_steps=min(steps)))
        else:
            steps.append(place.seek(target))
    return min(steps)


if __name__ == "__main__":
    lines = utils.read_inputs(12)
    print(f"answer: {main(lines)}")
