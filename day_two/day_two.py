import pytest

sample_input = "sample_input.txt"

minimum = {"red":0, "green":0, "blue":0} #r,g,b of bag

def solution(filename):
    f = open(filename) 
    lines = f.readlines()
    sum = 0

    for line in lines:
        start_index = line.find(":")
        game_id = line[5:start_index]
        print("Game {}".format(game_id))
        if start_index != -1:
            # get all games
            line = line[start_index+1:].strip().split(";")
        print(line)

        for draws in line:
            # dictionary of rgb for each draw per game
            colors = {x.split()[1]:int(x.split()[0]) for x in draws.split(",")}

            print("colors: {}".format(colors))
            for key, value in colors.items():
                if colors[key] > minimum[key]:
                    minimum[key] = colors[key]

        cube_power = 1
        for key, value in minimum.items():
            cube_power *= minimum[key]
            # reset for next game
            minimum[key] = 0                

        sum += cube_power
    print(sum)
    return sum

def test_sample():
    assert(solution(sample_input) == 2286)

answer = solution('day_two.txt')

#test_sample()