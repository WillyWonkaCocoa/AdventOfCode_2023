import pytest, math

sample_input = "sample_input.txt"
sample_input_2 = "sample_input_2.txt"
sample_input_part_two = "sample_input_part_two.txt"

def solution(filename):
    f = open(filename) 
    lines = f.readlines()

    instructions = lines[0].strip()
    total_steps = 0
    curr_location = []
    steps_per_starting_point = []
    map = {}

    for line in lines[2:]:
        dest, dest_left, dest_right = line[:3], line[7:10], line[12:15]
        if dest[-1] == "A":
            curr_location.append(dest)
        map[dest] = (dest_left, dest_right)

    while(len(curr_location) > 0):
        direction = ""
        if total_steps == 0:
            direction = instructions[0]
        else:
            direction = instructions[total_steps % len(instructions)]

        for i in range(len(curr_location)):
            if direction == "L":
                curr_location[i] = map[curr_location[i]][0]
            elif direction == "R":
                curr_location[i] = map[curr_location[i]][1]
            else:
                print("Invalid direction!")

        total_steps += 1
        for location in curr_location:
            if location[-1] == "Z":
                steps_per_starting_point.append(total_steps)
                print("took {} steps to reach {}".format(total_steps, location))

        curr_location = [x for x in curr_location if x[-1] != "Z"]

    print(math.lcm(*steps_per_starting_point))
    return math.lcm(*steps_per_starting_point)


def test_sample():
    assert(solution(sample_input) == 2)

def test_sample_two():
    assert(solution(sample_input_2) == 6)

def test_sample_part_two():
    assert(solution(sample_input_part_two) == 6)

#answer = solution('day_eight.txt')

#test_sample()
#test_sample_two()
test_sample_part_two()