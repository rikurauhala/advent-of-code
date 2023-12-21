import math

input = [line.strip() for line in open("input.txt")]
nodes = input[2:]
network = {}
start_nodes = []

for node in nodes:
    start_node = node.split(" = ")[0]
    if start_node.endswith("A"):
        start_nodes.append(start_node)
    left_node = node.split("=")[1].split(",")[0].split("(")[1]
    right_node = node.split("=")[1].split(",")[1].split(")")[0].strip()
    network[start_node] = (left_node, right_node)

cycles = []

for node in start_nodes:
    steps = 0
    instructions = list(input[0])
    while not node.endswith("Z"):
        direction = instructions.pop(0)
        instructions.append(direction)
        match direction:
            case 'L':
                node = network[node][0]
            case 'R':
                node = network[node][1]
        steps += 1
    cycles.append(steps)

print(math.lcm(*cycles))
