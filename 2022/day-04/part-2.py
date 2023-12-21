def get_pairs():
    with open("input.txt", "r") as input:
        pairs = [line.rstrip() for line in input]
    return pairs


def main():
    pairs = get_pairs()

    overlap = 0
    for pair in pairs:
        s1 = int(pair.split(',')[0].split('-')[0])
        e1 = int(pair.split(',')[0].split('-')[1])
        s2 = int(pair.split(',')[1].split('-')[0])
        e2 = int(pair.split(',')[1].split('-')[1])
        if (s1 <= s2 and s2 <= e1) or (s2 <= s1 and s1 <= e2):
            overlap += 1

    print(f"The number of pairs where the ranges overlap is {overlap}")


if __name__ == "__main__":
    main()
