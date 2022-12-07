import pathlib
import typing

from . import utils


class File:
    def __init__(self, path: str, size: int) -> None:
        self.path = path
        self.size = size

    def __repr__(self) -> str:
        return f"{self.path}:{self.size}"


class Dir:
    def __init__(self, path: str) -> None:
        self.path = path
        self.size = 0
        self.files = []

    def add_file(self, file: File):
        if self.path in file.path:
            self.size += file.size
            self.files.append(file)

    def list_files(self):
        for file in self.files:
            print(file)

    def __repr__(self) -> str:
        return self.path + " " + str(self.size)


class FileSystem:
    def __init__(self) -> None:
        self.cwd = pathlib.Path("/")

    def cd(self, arg: str):
        if arg == "..":
            self.cwd = self.cwd.parent
        else:
            self.cwd = self.cwd / arg

    def get_cwd(self) -> str:
        return str(self.cwd)

    def get_absolute_path(self, path: str) -> str:
        return str(self.cwd / path)


def part1(dirs) -> int:
    limit = 100000
    small_dirs = [d for d in dirs if d.size < limit]
    answer = 0
    for d in small_dirs:
        answer += d.size
    return answer


def part2(dirs) -> int:
    total_size = 70000000
    target = 30000000
    root_dir = dirs[0]
    free_space = total_size - root_dir.size
    delete_limit = target - free_space
    candidates = [d for d in dirs if d.size >= delete_limit]
    candidates.sort(key=lambda x: x.size)
    return candidates[0].size


def main(data):
    fs = FileSystem()
    dirs = [Dir("/")]
    files = []
    while True:
        try:
            line = next(lines)
        except StopIteration:
            break
        if line.startswith("$ cd"):
            cd_arg = line.split()[-1]
            fs.cd(cd_arg)
        elif line.startswith("$ ls"):
            pass  # this is a no action really
        elif line.startswith("dir"):
            dirname = line.split()[-1]
            dirs.append(Dir(fs.get_absolute_path(dirname)))
        else:  # this is a file, yehaw!
            size = int(line.split()[0])
            name = line.split()[1]
            files.append(File(fs.get_absolute_path(name), size))
    for file in files:
        for d in dirs:
            d.add_file(file)
    print(part2(dirs))


if __name__ == "__main__":
    lines = utils.read_inputs(7)
    main(lines)
