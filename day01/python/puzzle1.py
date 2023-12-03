
from functools import reduce

test_input = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

def get_outside_digits(line: str) -> int:
    line = ''.join([char for char in line if char.isdigit()])
    return int(line[0] + line[-1])

def main():
    with open("../data/day01-data.txt") as input_file:
        puzzle_input = input_file.readlines()

    numbers = [get_outside_digits(value) for value in puzzle_input]
    print(reduce(lambda x, y: x + y, numbers))

main()