import re
import string

SYMBOLS = set(string.punctuation) - set(".")
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]    

def get_surrounding_values(lines, index, directions):
    surrounding_values = []
    num_rows = len(lines)
    num_cols = len(lines[0]) if num_rows > 0 else 0

    for dx, dy in directions:
        new_x, new_y = index[0] + dx, index[1] + dy
        if 0 <= new_x < num_rows and 0 <= new_y < num_cols:
            surrounding_values.append(lines[new_x][new_y])

    return surrounding_values

def process_lines(lines):
    total = 0

    for line_index, line in enumerate(lines):
        for match in re.finditer(r"\d+", line):  
            number = int(match.group(0))
            start_index, end_index = match.span()

            contains_symbol = False

            for index in range(start_index, end_index):
                if any(surrounding_char in SYMBOLS for surrounding_char in get_surrounding_values(lines, (line_index, index), DIRECTIONS)):
                    contains_symbol = True
                    break

            if contains_symbol:
                total += int(number)
    
    return total

def main():
    with open("../data/day03-data.txt") as input_file:
        puzzle_input = [line.strip() for line in input_file.readlines()]

    print(process_lines(puzzle_input))

main()