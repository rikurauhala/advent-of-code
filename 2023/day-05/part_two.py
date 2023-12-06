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
            continue
        values = [int(value) for value in line.split()]
        current_map.append(values)

    return list(maps.values())


def main():
    almanac = read_input()
    seeds = [int(seed) for seed in almanac[0].split(":")[1].strip().split(" ")]
    maps = get_maps(almanac[1:])
    locations = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]

    for map in maps:
        new_locations = []
        while len(locations) > 0:
            seed_start, seed_end = locations.pop()
            for line in map:
                destination_start = line[0]
                source_start = line[1]
                range_length = line[2]
                overlap_start = max(seed_start, source_start)
                overlap_end = min(seed_end, source_start + range_length)
                if overlap_start < overlap_end:
                    new_locations.append((
                        overlap_start - source_start + destination_start,
                        overlap_end - source_start + destination_start
                    ))
                    if overlap_start > seed_start:
                        locations.append((seed_start, overlap_start))
                    if seed_end > overlap_end:
                        locations.append((overlap_end, seed_end))
                    break
            else:
                new_locations.append((seed_start, seed_end))
        locations = new_locations.copy()

    print(min(locations)[0])


if __name__ == "__main__":
    main()
