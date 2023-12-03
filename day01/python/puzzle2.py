
from functools import reduce

test_input = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]

word_to_digit_map = {
    "one": "1e",
    "two": "2o",
    "three": "3e",
    "four": "4r",
    "five": "5e",
    "six": "6x",
    "seven": "7n",
    "eight": "8t",
    "nine": "9e",
}

def clean_string(line: str) -> int:
    result = ""
    for char in line:
        result += char
        for key in word_to_digit_map.keys():
            result = result.replace(key, word_to_digit_map[key])
    return result


def get_outside_digits(line: str) -> int:
    line = ''.join([char for char in line if char.isdigit()])
    return int(line[0] + line[-1])

def main():
    with open("../data/day01-data.txt") as input_file:
        puzzle_input = input_file.readlines()

    clean_input = [clean_string(value) for value in puzzle_input]
    numbers = [get_outside_digits(value) for value in clean_input]
    print(reduce(lambda x, y: x + y, numbers))

main()