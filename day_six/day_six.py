import pytest

sample_input = "sample_input.txt"

def solution(filename):
    f = open(filename) 
    lines = f.readlines()

    times = convert_to_list_of_num(lines[0])
    distances = convert_to_list_of_num(lines[1])

    if len(times) != len(distances):
        print("Length of times and distances are not equal!")
        return 0

    index = 0
    answer = 1
    for i in range(len(times)):
        num_ways_to_win = 0
        total_time = times[index]
        record_distance = distances[index]
        for hold_time in range(1, total_time):
            if (total_time - hold_time)*hold_time >record_distance:
                num_ways_to_win += 1
        
        answer *= num_ways_to_win
        index += 1

    return answer

def convert_to_list_of_num(lst):
    start_index = lst.find(":")
    if start_index != -1:
        lst = lst[start_index+1:].strip().split()
        lst = [int(x) for x in lst]

    return lst

def test_sample():
    assert(solution(sample_input) == 288)

answer = solution('day_six.txt')

#test_sample()