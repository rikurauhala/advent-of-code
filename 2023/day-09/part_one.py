histories = [list(map(int, line.split())) for line in open("input.txt", "r").readlines()]

total_sum = 0

for history in histories:
    sequences = []
    sequences.append(history)
    while not (len(set(sequences[-1])) == 1 and sequences[-1][0] == 0):
        sequence = []
        for i in range(1, len(sequences[-1])):
            sequence.append(sequences[-1][i] - sequences[-1][i-1])
        sequences.append(sequence)
    total_sum += sum(sequence[-1] for sequence in sequences)

print(total_sum)
