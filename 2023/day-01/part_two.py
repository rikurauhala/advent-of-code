def main():
    with open("input.txt", "r") as input_file:
        lines = [line.strip() for line in input_file]
        sum = 0

        digits = [
            ["1", "one"],
            ["2", "two"],
            ["3", "three"],
            ["4", "four"],
            ["5", "five"],
            ["6", "six"],
            ["7", "seven"],
            ["8", "eight"],
            ["9", "nine"],
        ]

        for line in lines:
            first_appearance = [-1 for _ in range(9)]
            last_appearance = [-1 for _ in range(9)]

            for i in range(9):
                digit = line.find(digits[i][0])
                letters = line.find(digits[i][1])

                if digit >= 0 and letters >= 0:
                    first_appearance[i] = min(digit, letters)
                elif digit >= 0:
                    first_appearance[i] = digit
                elif letters >= 0:
                    first_appearance[i] = letters

                digit = line.rfind(digits[i][0])
                letters = line.rfind(digits[i][1])

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
