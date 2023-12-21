patterns = [pattern.strip().split("\n") for pattern in open("input.txt").read().split("\n\n")]

def find_line_of_reflection(pattern):
    for row in range(1, len(pattern)):
        above = pattern[:row][::-1]
        below = pattern[row:]
        above = above[:len(below)]
        below = below[:len(above)]
        if above == below:
            return row
    return 0

summary = 0

for pattern in patterns:
    row = find_line_of_reflection(pattern)
    col = find_line_of_reflection([*zip(*pattern)])
    summary += row * 100 + col

print(summary)
