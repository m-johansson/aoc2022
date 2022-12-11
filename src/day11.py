from collections import deque

import typing

from pprint import pprint

from . import utils


class Item:
    def __init__(self, worry: int) -> None:
        self.value = worry
        self.max_worry = None

    def set_max_worry(self, max_worry: int):
        self.max_worry = max_worry

    def __mul__(self, factor):
        self.value = (self.value * int(factor)) % max_worry
        return self

    def __add__(self, part: int):
        self.value = (self.value + int(part)) % max_worry
        return self

    def is_divisible(self, denominator):
        return (self.value % denominator) == 0

    def __int__(self):
        return self.value

    def __pow__(self, power):
        self.value = self.value**power
        return self


class Monkey:
    def __init__(
        self,
        items: typing.List[Item],
        operation: typing.Callable,
        test: typing.Callable,
        true_target: int,
        false_target: int,
    ) -> None:
        self._inventory = deque(items)
        self._targets = {
            True: true_target,
            False: false_target,
        }
        self.operation = operation
        self.test = test
        self.inspections = 0

    def set_monkey_group(self, monkey_group):
        self.monkey_group = monkey_group

    def action(self):
        while self._inventory:
            worry = self._inventory.popleft()
            new_worry = self.inspect(worry)
            self.throw(new_worry)

    def inspect(self, old_worry: Item):
        self.inspections += 1
        new_worry = self.operation(old_worry)
        return new_worry

    def throw(self, item):
        test_success = self.test(item)
        target = self._targets[test_success]
        self.monkey_group[target].catch(item)

    def catch(self, item):
        self._inventory.append(item)

    def __repr__(self):
        return f"Inspections: {self.inspections}"

    def __mul__(self, other):
        return self.inspections * other.inspections


def is_divisible_factory(denominator: int) -> typing.Callable:
    return lambda x: x.is_divisible(denominator)


class OperationFactory:
    def operation_factory(
        self, operator: str, operands: typing.List[str]
    ) -> typing.Callable:
        match operator:
            case "*":
                return self.multiplication(operands)
            case "+":
                return self.addition(operands)
            case _:
                raise ValueError()

    @staticmethod
    def multiplication(operands):
        if all((o == "old" for o in operands)):
            return lambda x: x**2
        else:
            second_operand = int(operands[1])
            return lambda x: x * second_operand

    @staticmethod
    def addition(operands):
        if all((o == "old" for o in operands)):
            return lambda x: x * 2
        else:
            second = int(operands[1])
            return lambda x: x + second


def main(lines):
    of = OperationFactory()
    monkeys: typing.List[Monkey] = []
    global max_worry
    max_worry = 1
    for l in lines:
        match l.split():
            case ["Monkey", i]:
                pass
            case ["Starting", "items:", *items]:
                items_list = [Item(int(item.replace(",", ""))) for item in items]
            case ["Operation:", "new", "=", first, operator, second]:
                operation = of.operation_factory(operator, [first, second])
            case ["Test:", "divisible", "by", denominator]:
                max_worry *= int(denominator)
                test = is_divisible_factory(int(denominator))
            case ["If", "true:", "throw", "to", "monkey", target]:
                true_target = int(target)
            case ["If", "false:", "throw", "to", "monkey", target]:
                false_target = int(target)
                monkeys.append(
                    Monkey(
                        items=items_list,
                        operation=operation,
                        test=test,
                        true_target=true_target,
                        false_target=false_target,
                    )
                )
                del items_list, operation, test, true_target, false_target
            case []:
                # this is the empty line
                pass
            case _:
                raise ValueError()
    for monkey in monkeys:
        monkey.set_monkey_group(monkeys)
    for _ in range(10000):
        for monkey in monkeys:
            monkey.action()
    monkeys.sort(key=lambda x: x.inspections, reverse=True)
    return monkeys[0] * monkeys[1]


if __name__ == "__main__":
    lines = utils.read_inputs(11)
    print(main(lines))
