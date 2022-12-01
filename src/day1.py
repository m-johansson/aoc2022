import pathlib
import heapq

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
            heapq.heappush(calories, current)
            current = 0
    print(sum(heapq.nlargest(3, calories)))


if __name__ == "__main__":
    main()
