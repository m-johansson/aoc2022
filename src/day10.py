from . import utils


class CPU:
    def __init__(self) -> None:
        self.position = 0
        self.cycle_count = 1
        self.x = 1
        self.screen = ""

    def noop(self):
        self.cycle()

    def addx(self, value: int):
        self.cycle()
        self.cycle()
        self.x += value

    def cycle(self):
        self.cycle_count += 1
        self._draw()
        self.position += 1

    def _draw(self):
        screen_coord = self.position % 40
        if screen_coord == 0:
            self.screen += "\n"
        if abs(screen_coord - self.x) <= 1:
            self.screen += "#"
        else:
            self.screen += "."


if __name__ == "__main__":
    lines = utils.read_inputs(10)
    cpu = CPU()
    for line in lines:
        match line.split():
            case ["noop"]:
                cpu.noop()
            case ["addx", value]:
                cpu.addx(int(value))
    print(cpu.screen)
