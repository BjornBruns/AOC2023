from typing import Dict, List
from functools import reduce

def process_games(games: List[str]) -> Dict[int, Dict[str, int]]:
    game_data = {}

    for game in games:
        game = game.strip()
        game_number, color_data = game.split(': ')
        game_number = int(game_number.split(' ')[1])

        game_data[game_number] = {}

        for segment in color_data.split('; '):
            colors = segment.split(', ')
            for color in colors:
                count, color_name = color.split(' ')
                count = int(count)

                if color_name in game_data[game_number]:
                    game_data[game_number][color_name] = max(game_data[game_number][color_name], count)
                else:
                    game_data[game_number][color_name] = count

    return game_data


def get_games_power_sum(game_data: Dict[int, Dict[str, int]]) -> int: 
    return sum([reduce((lambda x, y: x * y), colors.values()) for _, colors in game_data.items()])

def main():
    with open("../data/day02-data.txt") as input_file:
        puzzle_input = input_file.readlines()
    
    print(get_games_power_sum(process_games(puzzle_input)))

main()