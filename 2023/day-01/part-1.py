def main():
    with open("input.txt", "r") as input:
        lines = [line.strip() for line in input]
        sum = 0

        for line in lines:
            first = ""
            last = ""
            for char in line:
                if char in "0123456789":
                    if first == "":
                        first = char
                    if first != "":
                        last = char
            sum += int(first + last)

        print(sum)


if __name__ == "__main__":
    main()
