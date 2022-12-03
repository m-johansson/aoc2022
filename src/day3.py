from . import utils
import typing


def _score(char:str) -> int:
    if char.islower():
        score = ord(char) % ord("a") + 1
    elif char.isupper():
        score = ord(char) % ord("A") + 27
    else:
        raise ValueError()
    return score


def part1(packing_list:typing.Sequence[str]):
    score = 0
    for pack in packing_list:
        pack = pack.strip()
        mid_index = int(len(pack)/2)
        first_compartment = pack[:mid_index]
        second_compartment = pack[mid_index:]
        assert len(first_compartment) == len(second_compartment)
        intersection = set(first_compartment).intersection(second_compartment)
        assert len(intersection) == 1
        char:str = intersection.pop()
        score += _score(char)
    return score

def get_three_lines(packing_list):
    while True:
        try:
            yield (next(packing_list), next(packing_list), next(packing_list))
        except StopIteration:
            return
    

def part2(packing_list):
    score = 0
    for three_lines in get_three_lines(packing_list):
        sets = [set(line.strip()) for line in three_lines]
        intersection = sets[0].intersection(sets[1], sets[2])
        char:str = intersection.pop()
        score += _score(char)
    return score



if __name__=="__main__":
    packing_list = utils.read_inputs(3)
    print(part2(packing_list))
