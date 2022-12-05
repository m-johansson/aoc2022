from collections import deque
import typing
import re
import string

from . import utils


class LoadingZone:
    def __init__(self) -> None:
        self._stacks = {k: deque() for k in range(1, 10)}

    def add_crate(self, index: int, crate: str):
        """Specifically for the inputs, we build the pile in reverse"""
        self._stacks[index].appendleft(crate)

    def move_crates_one_at_a_time(self, source: int, target: int, iterations: int):
        for _ in range(iterations):
            crate = self._stacks[source].pop()
            self._stacks[target].append(crate)

    def move_crates_preserve_order(self, source: int, target: int, amount: int):
        crates = deque()
        for _ in range(amount):
            crates.append(self._stacks[source].pop())
        crates.reverse()
        self._stacks[target].extend(crates)

    def get_top_crates(
        self,
    ):
        top_crates = ""
        for stack in self._stacks.values():
            top_crates += stack.pop()
        return top_crates


class MoveReader:
    def __init__(self) -> None:
        self.pattern = re.compile(r"move (\d*) from (\d*) to (\d*)")

    def read_moves(self, line: str) -> typing.List[int]:
        result = self.pattern.match(line)
        l = [int(i) for i in result.groups()]
        assert (len(l)) == 3
        return l[0], l[1], l[2]  # amount, source, target


def crate_reader(line):
    for i in range(0, len(line), 4):
        yield line[i + 1]


def main(data):
    lz = LoadingZone()
    for line in data:
        if line == "\n":
            break
        for index, crate in enumerate(crate_reader(line)):
            if crate in string.ascii_letters:
                lz.add_crate(index + 1, crate)
    mr = MoveReader()
    for line in data:
        amount, source, target = mr.read_moves(line)
        lz.move_crates_preserve_order(source, target, amount)
    print(lz.get_top_crates())


if __name__ == "__main__":
    data = utils.read_inputs(5)
    main(data)
