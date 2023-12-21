def get_datastream():
    with open("input.txt", "r") as input:
        datastream = [line.rstrip() for line in input]
    return datastream[0]


def main():
    data = get_datastream()
    for i in range(len(data)):
        letters = set()
        for j in range(14):
            letters.add(data[i+j])
        if len(letters) == 14:
            print(f"Characters processed before the first marker: {i+14}")
            break


if __name__ == "__main__":
    main()
