def read_input():
    with open("input.txt", "r") as input:
        return [line.strip() for line in input]


def get_maps(lines):
    maps = {
        "seed-to-soil": [],
        "soil-to-fertilizer": [],
        "fertilizer-to-water": [],
        "water-to-light": [],
        "light-to-temperature": [],
        "temperature-to-humidity": [],
        "humidity-to-location": []
    }

    current_map = None

    for line in lines:
        if line == "":
            continue
        if ":" in line:
            map_type = line.split(":")[0].split(" ")[0]
            current_map = maps[map_type]
        else:
            values = [int(value) for value in line.split()]
            current_map.append(values)

    return list(maps.values())


def main():
    almanac = read_input()
    locations = [int(seed) for seed in almanac[0].split(":")[1].strip().split(" ")]
    maps = get_maps(almanac[1:])

    for map in maps:
        new_locations = locations.copy()
        for line in map:
            destination_range_start = line[0]
            source_range_start = line[1]
            range_length = line[2]
            for index, seed in enumerate(locations):
                if seed >= source_range_start and seed < source_range_start + range_length:
                    new_locations[index] = seed + destination_range_start - source_range_start
        locations = new_locations.copy()
    
    print(min(locations))


if __name__ == "__main__":
    main()
