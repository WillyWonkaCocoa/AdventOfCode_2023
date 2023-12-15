import pytest

sample_input = "sample_input.txt"

def solution(filename):
    f = open(filename) 
    lines = f.readline()
    sum = 0
    

    sequence = lines.strip().split(",")
    for piece in sequence:
        curr_value = 0
        for char in piece:
            curr_value += ord(char)
            curr_value *= 17
            curr_value %= 256
        print("{} becomes {}".format(piece, curr_value))
        sum += curr_value


    return sum

def test_sample():
    assert(solution(sample_input) == 1320)

answer = solution('day_fifteen.txt')
print(answer)

#test_sample()