import pytest

sample_input = "sample_input.txt"
sample_input_2 = "sample_input_2.txt"

def solution(filename):
    f = open(filename) 
    lines = f.readlines()

    instructions = lines[0].strip()
    print(instructions)
    total_steps = 0
    curr_location = "AAA"
    destination = "ZZZ"
    map = {}

    for line in lines[2:]:
        dest, dest_left, dest_right = line[:3], line[7:10], line[12:15]
        print("dest {} = ({}, {})".format(dest, dest_left, dest_right))
        map[dest] = (dest_left, dest_right)

    while(curr_location != destination):
        direction = ""
        print("currently at {}: checking index {} of directions: {} for {}: {}".format(curr_location, total_steps % len(instructions), instructions, curr_location, map[curr_location]))
        print("total steps {} % {} is {}".format(total_steps, len(instructions), total_steps % len(instructions)))
        if total_steps == 0:
            direction = instructions[0]
        else:
            direction = instructions[total_steps % len(instructions)]

        if direction == "L":
            curr_location = map[curr_location][0]
        elif direction == "R":
            curr_location = map[curr_location][1]
        else:
            print("Invalid direction!")

        print("now at: {}".format(curr_location))

        total_steps += 1
    
    print(total_steps)
    return total_steps


def test_sample():
    assert(solution(sample_input) == 2)

def test_sample_two():
    assert(solution(sample_input_2) == 6)

#answer = solution('day_eight.txt')

test_sample()
test_sample_two()