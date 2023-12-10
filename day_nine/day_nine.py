import pytest

sample_input = "sample_input.txt"

def solution(filename):
    f = open(filename) 
    lines = f.readlines()
    sum = 0

    for line in lines:
        line = line.strip().split()
        line = [int(x) for x in line]
        temp = line[0] - find_next_in_line(line)
        print("next in {} is: {}".format(line, temp))
        sum += temp
        
    print(sum)
    return sum

def find_next_in_line(line):
    next_num = 0
    prev_num = line[0]
    new_line = []
    for i in range(1, len(line)):
        temp = line[i] - prev_num
        prev_num = line[i]
        new_line.append(temp)

    if len(set(new_line)) == 1:
        # all the same number
        return new_line[0]
    else:
        return new_line[0] - find_next_in_line(new_line)

def test_sample():
    assert(solution(sample_input) == 114)

answer = solution('day_nine.txt')

test_sample()

part_two_sample = [10,  13,  16,  21,  30,  45]

def test_part_two():
    assert(find_next_in_line(part_two_sample) == 5)
