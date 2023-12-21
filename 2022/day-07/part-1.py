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

    sum_of_total_sizes = 0
    for size in directories.values():
        if size <= 100000:
            sum_of_total_sizes += size
    print(sum_of_total_sizes)


if __name__ == "__main__":
    main()
