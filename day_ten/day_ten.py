import pytest
sample_inputs = {"sample_input.txt": 4, "sample_input_two.txt": 8}
sample_inputs_part_two = {"day_ten_part_two_sample_input_one.txt": 4, \
                          "day_ten_part_two_sample_input_two.txt": 8, \
                            "day_ten_part_two_sample_input_three.txt": 10}

def solution(filename):
    f = open(filename) 
    lines = f.readlines()
    map = []
    s_location = (0,0)
    max_steps = 0

    x_index, y_index = 0, 0
    for line in lines:
        map.append([x for x in line.strip()])
    
        if "S" in map[x_index]:
            s_location = (x_index, map[x_index].index("S"))
        x_index += 1

    max_steps = find_len_of_path(s_location, map) // 2
    print(max_steps)
    return max_steps

def find_len_of_path(s_coord, map):
    total_steps = 1
    prev_coord = s_coord
    curr_coord = find_connecting_pipe(s_coord, s_coord, map)
    while(map[curr_coord[0]][curr_coord[1]] != "S"):
        tmp = curr_coord
        curr_coord = find_connecting_pipe(curr_coord, prev_coord, map)
        prev_coord = tmp
        total_steps += 1

    return total_steps
    
def find_connecting_pipe(coord, prev_coord, map):
    pipe_piece_map = {
        "|":["TOP", "BOTTOM"], \
        "-":["LEFT", "RIGHT"], \
        "L":["TOP", "RIGHT"],  \
        "J":["TOP", "LEFT"],   \
        "F":["RIGHT", "BOTTOM"], \
        "7":["LEFT", "BOTTOM"], \
        "S":["TOP", "LEFT", "RIGHT", "BOTTOM"] \
    }
    direction_to_piece_map = {
        "TOP":["|","7","F", "S"], \
        "LEFT":["-","L","F", "S"], \
        "RIGHT":["-","7","J", "S"], \
        "BOTTOM": ["|","L","J", "S"] \
    }

    x_lim = len(map) - 1
    y_lim = len(map[0]) - 1
    x_coord, y_coord, = coord[0], coord[1]
    directions_to_check = pipe_piece_map[map[x_coord][y_coord]]

    for dir in directions_to_check:
        if dir == "TOP" and x_coord - 1 >=  0 and \
            not (x_coord - 1 == prev_coord[0] and y_coord == prev_coord[1]):

            if map[x_coord - 1][y_coord] in direction_to_piece_map["TOP"]:
                return (x_coord - 1,y_coord)
        elif dir == "BOTTOM" and x_coord + 1 <= x_lim and \
            not (x_coord + 1 == prev_coord[0] and y_coord == prev_coord[1]):

            if map[x_coord + 1][y_coord] in direction_to_piece_map["BOTTOM"]:
                return (x_coord + 1,y_coord)
        elif dir == "LEFT" and y_coord - 1 >= 0 and \
            not (x_coord == prev_coord[0] and y_coord - 1 == prev_coord[1]):

            if map[x_coord][y_coord - 1] in direction_to_piece_map["LEFT"]:
                return (x_coord,y_coord-1)
        elif dir == "RIGHT" and y_coord + 1 <= y_lim and \
            not (x_coord == prev_coord[0] and y_coord + 1 == prev_coord[1]): 

            if map[x_coord][y_coord + 1] in direction_to_piece_map["RIGHT"]:
                return (x_coord,y_coord+1)

def test_samples():
    for key, value in sample_inputs.items(): 
        assert(solution(key) == value)

def test_samples_part_two():
    for key, value in sample_inputs_part_two.items():
        assert(solution(key) == value)

#answer = solution('day_ten.txt')

test_samples()
test_samples_part_two()