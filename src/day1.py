
import pathlib

def read_inputs():
    filepath = pathlib.Path(__file__).parent.parent / "inputs/day1.txt" 
    with open(filepath) as fid:
        yield from fid


def main():
    lines = read_inputs()
    largest = 0
    current = 0
    for l in lines:
        if l != "\n":
            current += int(l)
        else:
            if current > largest:
                largest = current
    print(largest)


if __name__ == "__main__":
    main()
