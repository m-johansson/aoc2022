from . import utils


class Section:
    def __init__(self, lower: int, upper: int) -> None:
        self.lower = lower
        self.upper = upper
        self.range = set(range(lower, upper + 1))

    def contains(self, other_section):
        return self.range.issuperset(other_section.range)

    def overlaps(self, other_section):
        return not self.range.isdisjoint(other_section.range)


def get_section_boundaries(line: str, section: int):
    return [int(i) for i in line.split(",")[section].split("-")]


def main():
    inputs = utils.read_inputs(4)
    fully_contained = 0
    any_overlap = 0
    for line in inputs:
        sections = []
        for i in range(2):
            bounds = get_section_boundaries(line, i)
            sections.append(Section(bounds[0], bounds[1]))
        if sections[0].contains(sections[1]) or sections[1].contains(sections[0]):
            fully_contained += 1
        if sections[0].overlaps(sections[1]):
            any_overlap += 1
    return fully_contained, any_overlap


if __name__ == "__main__":
    print(main())
