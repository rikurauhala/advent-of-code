sequence = open("input.txt").readline().strip().split(",")

total_sum = 0

for step in sequence:
    value = 0
    for char in step:
        value += ord(char)
        value *= 17
        value %= 256
    total_sum += value

print(total_sum)
