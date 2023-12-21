def get_datastream():
    with open("input.txt", "r") as input:
        datastream = [line.rstrip() for line in input]
    return datastream[0]


def main():
    data = get_datastream()
    for i in range(len(data)):
        letters = set([data[i], data[i+1], data[i+2], data[i+3]])
        if len(letters) == 4:
            print(f"Characters processed before the first marker: {i+4}")
            break


if __name__ == "__main__":
    main()
