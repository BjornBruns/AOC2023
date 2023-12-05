def process_lines(lines):
    total = 0

    for card in lines:
        _, card_data = card.split(': ')
        winning_numbers, scratched_numbers = card_data.split(' | ')

        winning_numbers = {int(num) for num in winning_numbers.split(' ') if num.isdigit()}
        scratched_numbers = {int(num) for num in scratched_numbers.split(' ') if num.isdigit()}

        common_elements = winning_numbers & scratched_numbers

        if common_elements:
            total += 2 ** (len(common_elements) - 1)

    return total

def main():
    with open("../data/day04-data.txt") as input_file:
        puzzle_input = [line.strip() for line in input_file]

    print(process_lines(puzzle_input))

main()
