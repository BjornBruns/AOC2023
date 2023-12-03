from functools import reduce
import re
import string
from collections import defaultdict

SYMBOLS = set(string.punctuation) - set(".")
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]    

def get_gear_locations(lines, index, directions):
    gear_locations = []
    num_rows = len(lines)
    num_cols = len(lines[0]) if num_rows > 0 else 0

    for dx, dy in directions:
        new_x, new_y = index[0] + dx, index[1] + dy
        if 0 <= new_x < num_rows and 0 <= new_y < num_cols:
            if lines[new_x][new_y] == "*":
                gear_locations.append((new_x, new_y))

    return gear_locations

def process_lines(lines):
    gears = defaultdict(list)
    total = 0

    for line_index, line in enumerate(lines):
        for match in re.finditer(r"\d+", line):  
            number = int(match.group(0))
            start_index, end_index = match.span()

            gear_locations = []
            for index in range(start_index, end_index):
                gear_locations.extend(get_gear_locations(lines, (line_index, index), DIRECTIONS))
                
            for location in set(gear_locations):
                gears[location].append(number)

    for numbers in gears.values():
        if len(numbers) == 2:
            total += reduce(lambda x, y: x*y, numbers)
    
    return total

def main():
    with open("../data/day03-data.txt") as input_file:
        puzzle_input = [line.strip() for line in input_file.readlines()]

    print(process_lines(puzzle_input))

main()