def get_rucksacks():
    with open("input.txt", "r") as input:
        rucksacks = [line.rstrip() for line in input]
    return rucksacks


def get_priority():
    priority = {}
    for n in range(1, 27):
        priority[chr(n+96)] = n
        priority[chr(n+64)] = n + 26
    return priority


def main():
    rucksacks = get_rucksacks()
    priority = get_priority()

    sum_of_priorities = 0
    for i in range(0, 300, 3):
        rucksack_1 = set(rucksacks[i])
        rucksack_2 = set(rucksacks[i+1])
        rucksack_3 = set(rucksacks[i+2])
        common_item = rucksack_1 & rucksack_2 & rucksack_3
        sum_of_priorities += priority[common_item.pop()]

    print(f"The sum of priorities is {sum_of_priorities}")


if __name__ == "__main__":
    main()
