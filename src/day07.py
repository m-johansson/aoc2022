import pathlib
import typing

from . import utils

class File:

    def __init__(self, path:str, size:int) -> None:
        self.path = path
        self.size = size

class Dir:

    def __init__(self, path:str) -> None:
        self.path = path
        self.size = 0
        self.files = []

    def add_file(self, file:File):
        if self.path in file.path:
            self.size += file.size
            self.files.append(file)

    def __repr__(self) -> str:
        return self.path + " " + str(self.size) 


class FileSystem:

    def __init__(self) -> None:
        self.cwd = pathlib.Path("/")

    def cd(self, arg:str):
        if arg == "..":
            self.cwd = self.cwd.parent
        else:
            self.cwd = self.cwd / arg

    def get_cwd(self) -> str:
        return str(self.cwd)
        



def main(data):
    fs = FileSystem()
    dirs = []
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
            pass #this is a no action really
        elif line.startswith("dir"):
            dirname = line.split()[-1]
            dirs.append(Dir(fs.get_cwd()+f"/{dirname}"))
        else: #this is a file, yehaw!
            size = int(line.split()[0])
            name = line.split()[1]
            files.append(File(fs.get_cwd() + f"/{name}", size))


    for file in files:
        for d in dirs:
            d.add_file(file)
    limit = 100000
    small_dirs = [d for d in dirs if d.size < limit]
    answer = 0
    for d in small_dirs:
        answer += d.size
    print(answer)
    print(dirs)
    return answer





if __name__=="__main__":
    lines = utils.read_inputs(7)
    next(lines) # throw away "$ cd /" as we're already having cwd /
    main(lines)
