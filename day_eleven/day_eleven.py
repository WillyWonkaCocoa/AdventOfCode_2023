import pytest
from itertools import combinations
sample_inputs = {"sample_input.txt": 374}

def solution(filename):
    f = open(filename) 
    lines = f.readlines()
    map = []
    new_map = []
    galaxy_coords = []
    galaxy_rows = []
    galaxy_cols = []
    sum_of_shortest_len = 0

    for line in lines:
        map.append([x for x in line.strip()])

    for x in range(len(map)):
        for y in range(len(map[0])):
            if map[x][y] == "#":
                galaxy_rows.append(x)
                galaxy_cols.append(y)
                galaxy_coords.append((x, y))

    galaxy_rows = set(galaxy_rows)
    galaxy_cols = set(galaxy_cols)
    galaxy_combos = list(combinations(galaxy_coords, 2))
    print(galaxy_coords)
    print("Out of {} galaxies we get {} combinations.".format(len(galaxy_coords), len(galaxy_combos)))

    for combo in galaxy_combos:
        galaxy_one, galaxy_two = combo[0], combo[1]
        x_start, x_end = min(galaxy_one[0], galaxy_two[0]), max(galaxy_one[0], galaxy_two[0])
        y_start, y_end = min(galaxy_one[1], galaxy_two[1]), max(galaxy_one[1], galaxy_two[1])
        steps = 0

        print("calculating shortest distance between {} and {}".format(galaxy_one, galaxy_two))

        for i in range(x_start+1, x_end+1):
            if i in galaxy_rows:
                steps += 1
            else:
                steps += 2

        for j in range(y_start+1, y_end+1):
            if j in galaxy_cols:
                steps += 1
            else:
                steps += 2
        print("shortest distance: {}".format(steps))
        sum_of_shortest_len += steps

    print(sum_of_shortest_len)    
    return sum_of_shortest_len

def test_samples():
    for key, value in sample_inputs.items(): 
        assert(solution(key) == value)

answer = solution('day_eleven.txt')

#test_samples()