import pytest

sample_input = "sample_input_day_two.txt"

def solution(filename):
    f = open(filename) 
    lines = f.read().split('\n')
    lines = [list(line) for line in lines]
    #print(lines)
    x,y = 0, 0
    x_dim = len(lines)
    y_dim = len(lines[0])
    gears = {} # hashmap of gears to adjacent numbers
    sum = 0
    
    for row in lines:
        num = ""
        adjacent_gears = set()
        isAdjacent = False
        is_part_of_num = False
        for c in row:
            print("current char: {}".format(c))
            if c.isdigit():
                num = num + c
                is_part_of_num = True

                # check adjacent coordinateelif 
                if  x-1 >= 0 and is_gear(lines[x-1][y]):
                    isAdjacent = True
                    adjacent_gears.add((x-1,y))
                elif x+1 < x_dim and is_gear(lines[x+1][y]):
                    isAdjacent = True
                    adjacent_gears.add((x+1,y))
                elif y-1 >= 0 and is_gear(lines[x][y-1]):
                    isAdjacent = True
                    adjacent_gears.add((x,y-1))
                elif y+1 < y_dim and is_gear(lines[x][y+1]):
                    isAdjacent = True
                    adjacent_gears.add((x,y+1))
                elif x-1 >= 0 and y-1 >= 0 and is_gear(lines[x-1][y-1]):
                    isAdjacent = True
                    adjacent_gears.add((x-1,y-1))
                elif x-1 >= 0 and y+1 < y_dim and is_gear(lines[x-1][y+1]):
                    isAdjacent = True
                    adjacent_gears.add((x-1,y+1))
                elif x+1 < x_dim and y-1 >= 0 and is_gear(lines[x+1][y-1]):
                    isAdjacent = True
                    adjacent_gears.add((x+1,y-1))
                elif x+1 < x_dim and y+1 < y_dim and is_gear(lines[x+1][y+1]):
                    isAdjacent = True
                    adjacent_gears.add((x+1,y+1))
                    
            if (not c.isdigit() or y == y_dim - 1) and is_part_of_num:
                # symbol or period following a number, or a number at the end of the line
                # check if adjacent to symbol
               
                if isAdjacent:
                    # add to dictionary of gear and adjacent numbers
                    print("adjacent gears: {}".format(adjacent_gears))
                    for adjacent_gear in adjacent_gears:
                        if adjacent_gear in gears:
                            gears[adjacent_gear].append(int(num))
                            print("adding num: {} to gears: {}".format(num, gears))
                        else:
                            gears[adjacent_gear] = [int(num)]
                            print("adding num: {} to gears: {}".format(num, gears))
                
                # reset
                num = ""
                adjacent_gears = set()
                is_part_of_num = False
                isAdjacent = False
            y += 1
        x += 1
        y = 0

    for key in gears:
        # if gear has exactly two adjacent numbers, multiply and add product to total sum
        value = gears[key]
        print("* at coordinate {} is adjacent to {}".format(key, value))
        if len(value) == 2:
            sum += value[0] * value[1]
    print(sum)
    return sum

def is_gear(c):
    return (c == '*')

def test_sample():
    assert(solution(sample_input) == 467835)

answer = solution('day_three.txt')
print(answer)
#test_sample()