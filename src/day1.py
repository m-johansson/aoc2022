import pathlib

def read_inputs():
    filepath = pathlib.Path(__file__).parent.parent / "inputs/day1.txt" 
    with open(filepath) as fid:
        yield from fid


def main():
    lines = read_inputs()
    calories = []
    current = 0
    for l in lines:
        if l != "\n":
            current += int(l)
        else:
            calories.append(current)
            current = 0
    calories.sort(reverse=True)
    print(calories)
    print(sum(calories[0:3]))


if __name__ == "__main__":
    main()
