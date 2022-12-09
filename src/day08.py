from . import utils


def build_matrix(data):
    trees = []
    for line in data:
        trees.append([int(c) for c in line.strip()])
    return trees


def is_taller(height, iterable):
    return all((h < height for h in iterable))


def visible_trees(height, iterable):
    tree_count = 0
    for h in iterable:
        tree_count+=1
        if h >= height:
            return tree_count
    return tree_count # this is reached on the edge

def get_col(data, col_index):
    col = [row[col_index] for row in data]
    return col

def part1(trees):
    count = 0
    for row_index, row in enumerate(trees):
        for col_index, height in enumerate(row):
            visible = is_taller(height, row[:col_index]) or is_taller(
                height, row[col_index + 1 :]
            )
            if not visible:
                col = get_col(trees, col_index)
                visible = is_taller(height, col[:row_index]) or is_taller(
                    height, col[row_index + 1 :]
                )
            if visible:
                count += 1
    return count

def part2(trees):
    max_score = 0
    for row_index, row in enumerate(trees):
        for col_index, height in enumerate(row):
            left = visible_trees(height, reversed(row[:col_index]))
            right = visible_trees(height, row[col_index+1:])
            col = get_col(trees,col_index)
            up = visible_trees(height, reversed(col[:row_index]))
            down = visible_trees(height, col[row_index+1:])
            score = left * right * up * down
            max_score = score if score > max_score else max_score
    return max_score

def main(data):
    trees = build_matrix(data)
    print(part2(trees))


if __name__ == "__main__":
    lines = utils.read_inputs(8)
    main(lines)
