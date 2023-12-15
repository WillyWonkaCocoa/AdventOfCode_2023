import pytest

sample_input = "sample_input.txt"

def solution(filename):
    f = open(filename) 
    lines = f.readline()
    sum = 0
    boxes = {}

    sequence = lines.strip().split(",")
    for piece in sequence:
        curr_value = 0
        label_end_index = 2
        if "-" in piece:
            label_end_index = piece.index("-")
        if "=" in piece:
            label_end_index = piece.index("=")
        label = piece[:label_end_index]
        operation = piece[label_end_index]
        for char in label:
            curr_value += ord(char)
            curr_value *= 17
            curr_value %= 256
        print("After \"{}\":".format(piece))
        
        if operation == "-":
            if curr_value in boxes:
                lenses = boxes[curr_value]
                index = 0
                found_index = -1
                for entry in lenses:
                    lens_label, focal_length = entry[0], entry[1]
                    if lens_label == label:
                        found_index = index
                    index += 1
                if found_index != -1:
                    del boxes[curr_value][found_index]

        elif operation == "=":
            focal_length = piece[label_end_index+1]
            if curr_value in boxes:
                lenses = boxes[curr_value]
                index = 0
                found_index = -1
                for entry in lenses:
                    if entry[0] == label:
                        found_index = index
                    index += 1
                if found_index != -1:
                    boxes[curr_value][found_index] = (label, focal_length)
                else: 
                    boxes[curr_value].append((label, focal_length))

            else:
                boxes[curr_value] = [(label, focal_length)]

        else:
            print("invalid operation: {} for label: {}".format(operation, label))
        
        #print(boxes)

    
    for box, lenses in boxes.items():
        box_sum = 0
        index = 1
        for lens in lenses:
            box_sum += (box+1) * index * int(lens[1])
            print("box {} sum for label {}: {} is {}".format(box, lens[0], lens[1], (box+1) * index * int(lens[1])))
            index += 1
        sum += box_sum

    print(sum)
    return sum

def test_sample():
    assert(solution(sample_input) == 145)

answer = solution('day_fifteen.txt')
print(answer)

#test_sample()