import pytest
import numpy as np

sample_input = "sample_input.txt"

def solution(filename):
    f = open(filename) 
    lines = f.readlines()
    seeds = lines[0]

    start_index = seeds.find(":")
    if start_index != -1:
        seeds = seeds[start_index+1:].strip().split()
        seeds = [int(x) for x in seeds]
    
    source = seeds
    mapping = []
    for line in lines[2:]:
        name = ""
        if line == "\n":
            # empty line
            source = source_to_destination_map(source, mapping)
            mapping = []
        elif line[-2:] == ":\n":
            # name of mapping
            name = line.strip()
        else:
            # number mappings
            mapping.append([int(x) for x in line.strip().split()])
    
    # last mapping: humidity-to-location map:
    source = source_to_destination_map(source, mapping)

    print(min(source))
    return min(source)

def source_to_destination_map(source_list, mapping):
    destination_list = []
    for item in source_list:
        has_mapping = False
        for i in range(len(mapping)):
            source_start, dest_start, range_len = mapping[i][1], mapping[i][0], mapping[i][2]
            if item >= source_start and item <= (source_start+range_len - 1):
                has_mapping = True
                destination_list.append(item - source_start + dest_start)
        if has_mapping == False:
            # map to itself
             destination_list.append(item)
    return destination_list

def test_sample():
    assert(solution(sample_input) == 35)

answer = solution('day_five.txt')

#test_sample()