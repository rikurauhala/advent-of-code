patterns = [pattern.strip().split("\n") for pattern in open("input.txt").read().split("\n\n")]

def count_differing_characters(row_above, row_below):
    return sum(1 for a, b in zip(row_above, row_below) if a != b)

def find_line_of_reflection(pattern):
    for row in range(1, len(pattern)):
        above = pattern[:row][::-1]
        below = pattern[row:]
        differing_characters = sum(
            count_differing_characters(row_above, row_below)
            for row_above, row_below in zip(above, below)
        )
        if differing_characters == 1:
            return row
    return 0

summary = 0

for pattern in patterns:
    row = find_line_of_reflection(pattern)
    col = find_line_of_reflection([*zip(*pattern)])
    summary += row * 100 + col

print(summary)
