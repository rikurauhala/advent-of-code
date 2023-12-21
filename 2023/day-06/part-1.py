input = [line.strip() for line in open("input.txt", "r").readlines()]
times = [int(time) for time in input[0].split(":")[1].strip().split()]
records = [int(distance) for distance in input[1].split(":")[1].strip().split()]
answer = 1

for race in range((len(times))):
    beats_the_record = 0
    for speed in range(1, times[race]):
        remaining = times[race] - speed
        distance = speed * remaining
        if distance > records[race]:
            beats_the_record += 1
    answer *= beats_the_record

print(answer)
