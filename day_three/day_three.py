import pytest

sample_input = "sample_input.txt"

def solution(filename):
    f = open(filename) 
    lines = f.read().split('\n')
    lines = [list(line) for line in lines]
    #print(lines)
    x,y = 0, 0
    x_dim = len(lines)
    y_dim = len(lines[0])
    sum = 0
    
    for row in lines:
        num = ""
        isAdjacent = False
        is_part_of_num = False
        for c in row:
            if c.isdigit():
                num = num + c
                is_part_of_num = True

                # check adjacent coordinates
                if  x-1 >= 0 and is_symbol(lines[x-1][y]) or \
                    x+1 < x_dim and is_symbol(lines[x+1][y]) or \
                    y-1 >= 0 and is_symbol(lines[x][y-1]) or \
                    y+1 < y_dim and is_symbol(lines[x][y+1]) or \
                    x-1 >= 0 and y-1 >= 0 and is_symbol(lines[x-1][y-1]) or \
                    x-1 >= 0 and y+1 < y_dim and is_symbol(lines[x-1][y+1]) or \
                    x+1 < x_dim and y-1 >= 0 and is_symbol(lines[x+1][y-1]) or \
                    x+1 < x_dim and y+1 < y_dim and is_symbol(lines[x+1][y+1]):
                        isAdjacent = True
                    
            if (not c.isdigit() or y == y_dim - 1) and is_part_of_num:
                # symbol or period following a number, or a number at the end of the line
                # check if adjacent to symbol
                if isAdjacent:
                    # add to sum
                    sum += int(num)

                # reset
                num = ""
                is_part_of_num = False
                isAdjacent = False
            y += 1
        x += 1
        y = 0
    return sum

def is_symbol(c):
    return (not c.isdigit() and c != '.')

def test_sample():
    assert(solution(sample_input) == 4361)

answer = solution('day_three.txt')
print(answer)
#test_sample()