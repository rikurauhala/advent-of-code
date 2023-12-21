def get_instructions():
    with open("input.txt", "r") as input:
        instructions = [line.rstrip() for line in input]
    return instructions


def get_crates():
    crates = [None for _ in range(9)]
    crates[0] = ['Z', 'J', 'N', 'W', 'P', 'S']
    crates[1] = ['G', 'S', 'T']
    crates[2] = ['V', 'Q', 'R', 'L', 'H']
    crates[3] = ['V', 'S', 'T', 'D']
    crates[4] = ['Q', 'Z', 'T', 'D', 'B', 'M', 'J']
    crates[5] = ['M', 'W', 'T', 'J', 'D', 'C', 'Z', 'L']
    crates[6] = ['L', 'P', 'M', 'W', 'G', 'T', 'J']
    crates[7] = ['N', 'G', 'M', 'T', 'B', 'F', 'Q', 'H']
    crates[8] = ['R', 'D', 'G', 'C', 'P', 'B', 'Q', 'W']
    return crates


def main():
    crates = get_crates()
    instructions = get_instructions()

    for instruction in instructions:
        quantity = int(instruction.split(' ')[1])
        origin = int(instruction.split(' ')[3]) - 1 
        target = int(instruction.split(' ')[5]) - 1
        crates[target] += crates[origin][-quantity:]
        crates[origin] = crates[origin][:-quantity]

    top_crates = ''.join([crate[-1] for crate in crates])
    print(f"Crates on top are {top_crates}")


if __name__ == "__main__":
    main()
