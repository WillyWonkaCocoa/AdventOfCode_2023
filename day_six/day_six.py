import pytest

sample_input = "sample_input.txt"

def solution(filename):
    f = open(filename) 
    lines = f.readlines()

    total_time = convert_to_list_of_num(lines[0])
    record_distance = convert_to_list_of_num(lines[1])
    num_ways_to_win = 0

    for hold_time in range(1, total_time):
        if (total_time - hold_time)*hold_time >record_distance:
            num_ways_to_win += 1

    return num_ways_to_win

def convert_to_list_of_num(lst):
    start_index = lst.find(":")
    if start_index != -1:
        lst = lst[start_index+1:].strip().split()
        lst = int("".join(lst))

    return lst

def test_sample():
    assert(solution(sample_input) == 71503)

answer = solution('day_six.txt')

#test_sample()