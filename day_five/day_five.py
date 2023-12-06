import pytest
from collections import deque

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
    print(source)
    for line in lines[2:]:
        name = ""
        if line == "\n":
            # empty line
            source = source_to_destination_map(source, mapping)
            print("mapped ranges: {}".format(source))
            mapping = []
        elif line[-2:] == ":\n":
            # name of mapping
            name = line.strip()
        else:
            # number mappings
            mapping.append([int(x) for x in line.strip().split()])
    
    # last mapping: humidity-to-location map:
    source = source_to_destination_map(source, mapping)
    print("mapped ranges: {}".format(source))
    print(source[::2])
    print(min(source[::2]))
    return min(source[::2]) # filter out ranges, just get smallest starting value

def source_to_destination_map(source_list, mapping):
    destination_list = []
    source_list = deque(source_list)
    while len(source_list) >= 2:
        item_start, item_range = source_list.popleft(), source_list.popleft()
        item_end = item_start + item_range - 1
        has_mapping = False

        for i in range(len(mapping)):
            source_start, dest_start, source_range = mapping[i][1], mapping[i][0], mapping[i][2]
            source_end = source_start + source_range - 1
            
            #print("start: {} range: {}, source_start: {} source_range: {}".format(item_start, item_range, source_start, source_range))
            if item_end < source_start or item_start > source_end:
                # item starts out of range (too small or too big)
                pass
            elif item_start >= source_start :
                # starts in range
                has_mapping = True
                map_start = item_start - source_start + dest_start

                if (item_start + item_range - 1) <= (source_start+source_range - 1):
                    # ends in range
                    # add mapped range to mapping
                    #print("source start of: {} and range of: {} is in range. Mapped to start: {} and range: {}".format(source_start, source_range, map_start, item_range))
                    destination_list.extend([map_start, item_range])

                else:
                    # ends out of range
                    # split into: 1) mapped range and add to mapping, 2) unmapped range add to source_list
                    map_range = source_start + source_range - item_start
                    destination_list.extend([map_start, map_range])
                    unmapped_start = item_start + map_range
                    unmapped_range = item_range - map_range
                    source_list.append(unmapped_start)
                    source_list.append(unmapped_range)

            elif item_start < source_start:
                has_mapping = True 
                map_start = dest_start

                # add lower unmapped range to be mapped
                unmapped_start = item_start
                unmapped_range = source_start - item_start
                source_list.append(unmapped_start)
                source_list.append(unmapped_range)
                
                if (item_end <= source_end):
                    # ends in range
                    # split into: 1) mapped range and add to mapping, 2) unmapped range add to source_list
                    map_range = item_end - source_start + 1
                    destination_list.extend([map_start, map_range])
                    
                else:
                    # ends out of range but covers range
                    # split into: 1) add mapped range to mapping, 2) unmapped upper range add to source_list
                    map_range = source_range
                    destination_list.extend([map_start, map_range])

                    unmapped_start = source_start + source_range
                    unmapped_range = item_end - unmapped_start
                    source_list.append(unmapped_start)
                    source_list.append(unmapped_range)

        if has_mapping == False:
            # map to itself
            destination_list.extend([item_start, item_range])
    return destination_list

def test_sample():
    assert(solution(sample_input) == 46)

answer = solution('day_five.txt')

#test_sample()