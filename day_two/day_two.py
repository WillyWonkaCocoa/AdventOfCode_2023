import pytest

sample_input = "sample_input.txt"

truth = {"red":12, "green":13, "blue":14} #r,g,b of bag

def solution(filename):
    f = open(filename) 
    lines = f.readlines()
    sum = 0

    for line in lines:
        is_valid = True
        start_index = line.find(":")
        game_id = line[5:start_index]
        print("Game {}".format(game_id))
        if start_index != -1:
            # get all games
            line = line[start_index+1:].strip().split(";")
        print(line)

        for draws in line:
            #dictionary of rgb for each draw per game
            colors = {x.split()[1]:int(x.split()[0]) for x in draws.split(",")}

            print("colors: {}".format(colors))
            for key, value in colors.items():
                if colors[key] > truth[key]:
                    is_valid = False
        if is_valid:
            game_id = int(game_id)
            sum += game_id
    print(sum)
    return sum

def test_sample():
    assert(solution(sample_input) == 8)

answer = solution('day_two.txt')

test_sample()