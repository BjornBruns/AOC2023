from typing import Dict, List

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


def get_id_sum(game_data: Dict[int, Dict[str, int]], red: int, green: int, blue: int) -> int: 
    accepted_ids = [
        game_id for game_id, colors in game_data.items()
        if colors['red'] <= red and colors['green'] <= green and colors['blue'] <= blue
    ]
    return sum(accepted_ids)

def main():
    with open("../data/day02-data.txt") as input_file:
        puzzle_input = input_file.readlines()

    
    print(get_id_sum(process_games(puzzle_input), 12, 13, 14))

main()