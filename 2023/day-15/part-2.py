sequence = open("input.txt").readline().strip().split(",")

def hash(label):
    hash = 0
    for char in label:
        hash = (hash + ord(char)) * 17 % 256
    return hash

boxes = [{} for _ in range(256)]

for step in sequence:
    match step.strip("-").split("="):
        case [label]:
            boxes[hash(label)].pop(label, None)
        case [label, focal_length]:
            boxes[hash(label)][label] = int(focal_length)

focusing_power = 0

for index, box in enumerate(boxes):
    if len(box) == 0:
        continue
    for slot, focal_length in enumerate(box.values()):
        focusing_power += ((index+1) * (slot+1) * focal_length)

print(focusing_power)
