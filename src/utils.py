import pathlib

def read_inputs(day:int):
    filepath = pathlib.Path(__file__).parent.parent / f"inputs/day{day}.txt" 
    with open(filepath) as fid:
        yield from fid
