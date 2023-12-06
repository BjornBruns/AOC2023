def line_to_ranges_tuples(map_lines):
    return [(int(source), int(source) + int(length) - 1, int(dest) - int(source)) for dest, source, length in (line.split() for line in map_lines)]
    
def conv(number, maps):
    for start, end, diff in maps:
        if start <= number <= end:
            return number + diff
    return number

def process_lines(lines):
    seeds = list(map(lambda x: int(x), lines[0].split(": ")[1].split(" ")))

    # Indexes of the first lines of each map
    sts_first_index = lines.index('seed-to-soil map:') + 1
    stf_first_index = lines.index('soil-to-fertilizer map:') + 1
    ftw_first_index = lines.index('fertilizer-to-water map:') + 1
    wtl_first_index = lines.index('water-to-light map:') + 1
    ltt_first_index = lines.index('light-to-temperature map:') + 1
    tth_first_index = lines.index('temperature-to-humidity map:') + 1
    htl_first_index = lines.index('humidity-to-location map:') + 1
    
    # Extracting map lines
    sts_maps = lines[(sts_first_index):(stf_first_index - 2)]
    stf_maps = lines[(stf_first_index):(ftw_first_index - 2)]
    ftw_maps = lines[(ftw_first_index):(wtl_first_index - 2)]
    wtl_maps = lines[(wtl_first_index):(ltt_first_index - 2)]
    ltt_maps = lines[(ltt_first_index):(tth_first_index - 2)]
    tth_maps = lines[(tth_first_index):(htl_first_index - 2)]
    htl_maps = lines[(htl_first_index):]

    sts_dict = line_to_ranges_tuples(sts_maps)
    stf_dict = line_to_ranges_tuples(stf_maps)
    ftw_dict = line_to_ranges_tuples(ftw_maps)
    wtl_dict = line_to_ranges_tuples(wtl_maps)
    ltt_dict = line_to_ranges_tuples(ltt_maps)
    tth_dict = line_to_ranges_tuples(tth_maps)
    htl_dict = line_to_ranges_tuples(htl_maps)

    locations = [conv(conv(conv(conv(conv(conv(conv(seed, sts_dict), stf_dict), ftw_dict), wtl_dict), ltt_dict), tth_dict), htl_dict) for seed in seeds]

    return min(locations)

def main():
    with open("../data/day05-data.txt") as input_file:
        puzzle_input = [line.strip() for line in input_file]

    print(process_lines(puzzle_input))

main()
