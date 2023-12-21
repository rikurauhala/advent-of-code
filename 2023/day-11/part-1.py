image = [line.strip() for line in open("input.txt")]

empty_rows = [index for index, row in enumerate(image) if set(row) == {"."}]
empty_cols = [index for index, col in enumerate(zip(*image)) if set(col) == {"."}]

galaxies = []

for row_index, row in enumerate(image):
    for col_index, char in enumerate(row):
        if char == "#":
            galaxies.append((row_index, col_index))

total_sum = 0

for index, (row1, col1) in enumerate(galaxies):
    for (row2, col2) in galaxies[:index]:
        for row in range(min(row1, row2), max(row1, row2)):
            total_sum += 2 if row in empty_rows else 1
        for col in range(min(col1, col2), max(col1, col2)):
            total_sum += 2 if col in empty_cols else 1

print(total_sum)
