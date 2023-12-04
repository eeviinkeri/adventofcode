import os
import re


class Game:
    def __init__(self, number, rounds):
        self.number = number
        self.rounds = rounds


def find_possible_games(games):
    '''
    Determine which games would have been possible if the bag had been loaded with only
    12 red cubes, 13 green cubes, and 14 blue cubes
    '''
    red_cubes = 12
    green_cubes = 13
    blue_cubes = 14
    impossible_games = list()
    for game in games:
        for round in game.rounds:
            if round['red'] > red_cubes or round['blue'] > blue_cubes or round['green'] > green_cubes:
                impossible_games.append(game.number)
    impossible_set = set(impossible_games)
    possible_games = list()
    for i in range(1, 101):
        if i not in impossible_set:
            possible_games.append(i)
    return possible_games


def find_min_cube_count(games):
    '''
    what is the fewest number of cubes of each color that could have been
    in the bag to make the game possible?
    '''
    min_cube_powers = list()
    for game in games:
        red = 0
        blue = 0
        green = 0
        for round in game.rounds:
            if round['red'] > red:
                red = round['red']
            if round['blue'] > blue:
                blue = round['blue']
            if round['green'] > green:
                green = round['green']
        min_cube_powers.append(red*blue*green)
    return min_cube_powers


def read_file_to_list(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def main():
    filename = f"{os.getcwd()}/data/input2.txt"
    colors = ["red", "blue", "green"]
    data = read_file_to_list(filename)

    # parse games
    games = list()
    for row in data:
        game_split = row.split(": ")
        game_name = game_split[0]
        game_id = int(re.findall(r'\d+', game_name)[0])
        game_rounds = game_split[1].split("; ")
        
        rounds = list()
        for round in game_rounds:
            cubes = round.split(", ")
            round = dict()
            for cube_color in cubes:
                num = int(re.findall(r'\d+', cube_color)[0])
                color = ''.join(re.findall(r"(?=("+'|'.join(colors)+r"))", cube_color))
                round[color] = num
            if "red" in round: pass
            else: round["red"] = 0
            if "blue" in round: pass
            else: round["blue"] = 0
            if "green" in round: pass
            else: round["green"] = 0
            rounds.append(round)
        games.append(Game(number=game_id, rounds=rounds))

    possible_games = find_possible_games(games)
    print("Answer to day2 part one is:", sum(possible_games))

    power_of_min_cube_set = find_min_cube_count(games)
    print("Answer to day2 part two is:", sum(power_of_min_cube_set))

if __name__ == "__main__":
    main()
