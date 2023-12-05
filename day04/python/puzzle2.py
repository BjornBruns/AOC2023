from collections import defaultdict

def process_lines(lines):
    cards = defaultdict(lambda: 1)

    for card in lines:
        card_number, card_data = card.split(': ')
        card_number = int(card_number.split(' ')[-1])

        winning_numbers, scratched_numbers = card_data.split(' | ')
        winning_numbers = {int(num) for num in winning_numbers.split(' ') if num.isdigit()}
        scratched_numbers = {int(num) for num in scratched_numbers.split(' ') if num.isdigit()}

        common_elements = len(winning_numbers & scratched_numbers)

        for _ in range(cards[card_number]):
            for i in range(card_number, card_number+common_elements):
                if i < len(lines):
                    cards[i+1] += 1
        
    return sum(cards.values())

def main():
    with open("../data/day04-data.txt") as input_file:
        puzzle_input = [line.strip() for line in input_file.readlines()]

    print(process_lines(puzzle_input))

main()