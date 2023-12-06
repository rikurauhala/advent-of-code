input = [line.strip() for line in open("input.txt", "r").readlines()]
time = int("".join(input[0].split(":")[1].strip().split()))
record = int("".join(input[1].split(":")[1].strip().split()))
beats_the_record = 0

for speed in range(1, time):
    remaining = time - speed
    distance = speed * remaining
    if distance > record:
        beats_the_record += 1

print(beats_the_record)
