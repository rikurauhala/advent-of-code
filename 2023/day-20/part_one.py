class Module:
    def __init__(self, name, type, destinations):
        self.name = name
        self.type = type
        self.destinations = destinations
        match type:
            case "%":
                self.memory = 0
            case "&":
                self.memory = {}

input = [line.strip() for line in open("input.txt").readlines()]

initial_pulses = None
modules = {}

for line in input:
    module, destinations = line.split(" -> ")
    destinations = [destination.strip() for destination in destinations.split(",")]
    if module == "broadcaster":
        initial_pulses = [("broadcaster", destination, "low") for destination in destinations]
        continue
    type = module[0]
    name = module[1:]
    modules[name] = Module(name, type, destinations)

for name, module in modules.items():
    for destination in module.destinations:
        if destination in modules and modules[destination].type == "&":
            modules[destination].memory[name] = "low"

def update_pulses(pulses, module):
    for destination in module.destinations:
        pulses.append((module.name, destination, new_pulse))
    return pulses

def get_new_pulse(module):
    if set(module for module in module.memory.values()) == {"high"}:
        return "low"
    return "high"

cycles = 1000
low = cycles
high = 0

for _ in range(cycles):
    pulses = initial_pulses.copy()
    while pulses:
        origin, destination, pulse = pulses.pop(0)
        match pulse:
            case "low":
                low += 1
            case "high":
                high += 1
        
        if destination not in modules:
            continue
        
        module = modules[destination]
            
        match module.type:
            case "%":
                if pulse == "high":
                    continue
                module.memory ^= 1
                new_pulse = "high" if module.memory == 1 else "low"
                pulses = update_pulses(pulses, module)
            case "&":
                module.memory[origin] = pulse
                new_pulse = get_new_pulse(module)
                pulses = update_pulses(pulses, module)

print(low * high)
