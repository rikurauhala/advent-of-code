def main():
    with open("input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file]

        strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

        sum = 0

        for line in lines:
            first_appearance = [-1 for _ in range(9)]
            last_appearance = [-1 for _ in range(9)]

            for i in range(9):
                digit = line.find(str(i+1))
                letters = line.find(strings[i])

                if digit >= 0 and letters >= 0:
                    first_appearance[i] = min(digit, letters)
                else:
                    first_appearance[i] = max(digit, letters)

                digit = line.rfind(str(i+1))
                letters = line.rfind(strings[i])

                if digit >= 0 and letters >= 0:
                    last_appearance[i] = max(digit, letters)
                elif digit >= 0:
                    last_appearance[i] = digit
                elif letters >= 0:
                    last_appearance[i] = letters

            first = first_appearance.index((min(i for i in first_appearance if i > -1))) + 1
            last = last_appearance.index((max(last_appearance))) + 1
            calibration_value = str(first) + str(last)
            sum += int(calibration_value)

        print(sum)


if __name__ == "__main__":
    main()
