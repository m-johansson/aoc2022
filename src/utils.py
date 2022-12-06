import pathlib


def read_inputs_as_single_string(day: int):
    filepath = pathlib.Path(__file__).parent.parent / f"inputs/day{day}.txt"
    with open(filepath) as fid:
        return fid.read()


def read_inputs(day: int):
    filepath = pathlib.Path(__file__).parent.parent / f"inputs/day{day}.txt"
    with open(filepath) as fid:
        yield from fid
