""" Note - this puzzle's solution was inspired by using an example of https://github.com/hyper-neutrino """

def parse_seed_inputs(seed_input_line):
    """ Parse the initial seed input line into a list of tuples. """
    seed_inputs = list(map(int, seed_input_line.split(":")[1].split()))
    return [(seed_inputs[i], seed_inputs[i] + seed_inputs[i + 1]) for i in range(0, len(seed_inputs), 2)]

def parse_transformation_block(block):
    """ Parse a transformation block into a list of transformation ranges. """
    return [list(map(int, line.split())) for line in block.splitlines()[1:]]

def process_seeds(seeds, ranges):
    """ Process seeds through transformation ranges and return the new seeds. """
    new_seeds = []
    for seed_start, seed_end in seeds:
        for dest_start, src_start, length in ranges:
            overlap_start, overlap_end = max(seed_start, src_start), min(seed_end, src_start + length)
            difference = dest_start - src_start 
            if overlap_start < overlap_end:
                new_seeds.append((overlap_start + difference, overlap_end + difference))
                if overlap_start > seed_start:
                    # Add back to seeds list as this part is not transformed yet
                    seeds.append((seed_start, overlap_start))
                if seed_end > overlap_end:
                    # Add back to seeds list as this part is not transformed yet
                    seeds.append((overlap_end, seed_end))
                break
        else:
            # If the break is not hit, then this will be executed
            new_seeds.append((seed_start, seed_end))
    return new_seeds

def process_lines(lines):
    """ Main function to process the lines of the file. """
    # Split file and assign first item to seeds_input_line, the rest to map_blocks
    seed_input_line, *map_blocks = lines.split("\n\n")
    seeds = parse_seed_inputs(seed_input_line)

    # Go over each of the transformation blocks one by one
    for block in map_blocks:
        transformation_ranges = parse_transformation_block(block)
        seeds = process_seeds(seeds, transformation_ranges)

    return min(seeds)[0]

def main():
    with open("../data/day05-data.txt") as input_file:
        puzzle_input = input_file.read()

    print(process_lines(puzzle_input))

main()