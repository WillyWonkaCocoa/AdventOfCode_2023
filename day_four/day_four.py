import pytest

sample_input = "sample_input.txt"

def solution(filename):
    f = open(filename) 
    lines = f.readlines()
    sum = 0

    for line in lines:
        start_index = line.find(":")
        card_id = line[5:start_index]
        if start_index != -1:
            # get all games
            winning_nums, scratched_nums = line[start_index+1:].strip().split("|")
        winning_nums = [int(x) for x in winning_nums.strip().split()]
        scratched_nums = [int(x) for x in scratched_nums.strip().split()]
        winning_dict = {x:1 for x in winning_nums}

        points_for_line = -1
        for num in scratched_nums:
            if num in winning_nums:
                if points_for_line == -1:
                    points_for_line = 1
                else:
                    points_for_line *= 2

        if points_for_line > 0:
            sum += points_for_line
    print(sum)
    return sum

def test_sample():
    assert(solution(sample_input) == 13)

answer = solution('day_four.txt')

#test_sample()