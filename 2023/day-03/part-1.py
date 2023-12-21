def is_symbol(char):
    return not (char.isdigit() or char == ".")


def get_full_number(schematic, row, col):
    current_char = schematic[row][col]
    left_part = ""
    right_part = ""
    i = col - 1
    while i >= 0 and schematic[row][i].isdigit():
        left_part = schematic[row][i] + left_part
        i -= 1
    i = col + 1
    while i < len(schematic[row]) and schematic[row][i].isdigit():
        right_part += schematic[row][i]
        i += 1
    full_number = left_part + current_char + right_part
    return full_number


def get_adjacent_numbers(schematic, x, y):
    adjacent_numbers = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            if not schematic[x + i][y + j].isdigit():
                continue
            adjacent_number = get_full_number(schematic, x + i, y + j)
            adjacent_numbers.add(int(adjacent_number))
    return adjacent_numbers


def main():
    with open("input.txt", "r") as input:
        schematic = [line.strip() for line in input]
        total_sum = 0
        for x, line in enumerate(schematic):
            for y, char in enumerate(line):
                if not is_symbol(char):
                    continue
                adjacent_numbers = get_adjacent_numbers(schematic, x, y)
                total_sum += sum(adjacent_numbers)
        print(total_sum)


if __name__ == "__main__":
    main()
