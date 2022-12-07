from collections import defaultdict
from itertools import accumulate


def get_input():
    with open("input.txt", "r") as input:
        input = [line.rstrip() for line in input]
    return input


def main():
    directories = defaultdict(int)
    input = get_input()
    path = []
    for line in input:
        match line.split():
            case "$", "cd", "..":
                path.pop()
            case "$", "cd", "/":
                path = [""]
            case "$", "cd", dir:
                path.append(dir)
            case "$", "ls":
                pass
            case "dir", _:
                pass
            case size, _:
                for dir in accumulate(path):
                    directories[dir] += int(size)

    size_of_dir_to_be_removed = 9999999
    unused_space = directories[""] - 40000000
    for size in directories.values():
        if size >= unused_space and size < size_of_dir_to_be_removed:
            size_of_dir_to_be_removed = size
    print(size_of_dir_to_be_removed)


if __name__ == "__main__":
    main()
