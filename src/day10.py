from . import utils


class CPU:

    def __init__(self) -> None:
        self.cycle = 0
        self.x = 1
        self.score_cycles = [20, 60, 100, 140, 180, 220]
        self.score = 0

    def noop(self):
        self.cycle += 1
        self._evaluate()

    def addx(self, value:int):
        self.cycle += 1
        self._evaluate()
        self.cycle += 1
        self._evaluate()
        self.x += value


    def _evaluate(self):
        if self.cycle in self.score_cycles:
            self.score += self.cycle*self.x

if __name__=="__main__":
    lines = utils.read_inputs(10)
    cpu = CPU()
    for line in lines:
        match line.split():
            case ["noop"]:
                cpu.noop()
            case ["addx", value]:
                cpu.addx(int(value))
    print(cpu.score)
