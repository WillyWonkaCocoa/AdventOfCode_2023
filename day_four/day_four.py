import pytest
import numpy as np

sample_input = "sample_input.txt"

def solution(filename):
    f = open(filename) 
    lines = f.readlines()
    cards = np.ones(len(lines)+1, dtype=int)
    index = 1

    for line in lines:
        start_index = line.find(":")
        card_id = line[5:start_index]
        if start_index != -1:
            # get all games
            winning_nums, scratched_nums = line[start_index+1:].strip().split("|")
        winning_nums = [int(x) for x in winning_nums.strip().split()]
        scratched_nums = [int(x) for x in scratched_nums.strip().split()]
        winning_dict = {x:1 for x in winning_nums}
        num_of_matches = 0

        for num in scratched_nums:
            if num in winning_nums:
                num_of_matches += 1

        for i in range(1, num_of_matches+1):
            cards[index+i] += cards[index]

        index += 1
    return sum(cards[1:])

def test_sample():
    assert(solution(sample_input) == 30)

answer = solution('day_four.txt')

#test_sample()