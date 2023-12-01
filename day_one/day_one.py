f = open('day_one.txt') 
lines = f.readlines()
sum = 0

for line in lines:
    nums = []
    print(line)

    max_i = len(line) - 1
    print("lenght of line is: {}".format(max_i))
    for i in range(len(line)):
        if line[i].isdigit():
            nums.append(int(line[i]))
        else:
            print("does {} equal to {}? {}".format(line[i], 's', line[i] == 's'))
            if line[i] == 'o': #one +2
                if i + 2 <= max_i and line[i:i+3] == "one":
                    nums.append(1)
            elif line[i] == 't': #two, ten, +2 three +4
                if i + 2 <= max_i and line[i:i+3] == "two":
                    nums.append(2)
                elif i + 2 <= max_i and line[i:i+3] == "ten":
                    nums.append(10)
                elif i + 4 <= max_i and line[i:i+5] == "three":
                    nums.append(3)
            elif line[i] == 'f': #four, five +3
                if i + 2 <= max_i and line[i:i+4] == "four":
                    nums.append(4)
                elif i + 2 <= max_i and line[i:i+4] == "five":
                    nums.append(5)
            elif line[i] == 's': #six, +2 seven +4
                print("potential number spelled starting with s!")
                print("i + 4 <= max_i is: {}".format(i + 4 <= max_i))
                print("line[i:i+4] == \"seven\" is: {}".format(line[i:i+4] == "seven"))
                print("line[i:i+4] is: {}".format(line[i:i+4]))
                if i + 2 <= max_i and line[i:i+3] == "six":
                    print("number is six")
                    nums.append(6)
                elif i + 4 <= max_i and line[i:i+5] == "seven":
                    print("number is seven")
                    nums.append(7)
            elif line[i] == 'e': #eight +4
                if i + 4 <= max_i and line[i:i+5] == "eight":
                    nums.append(8)
            elif line[i] == 'n': #nine +3
                if i + 3 <= max_i and line[i:i+4] == "nine":
                    nums.append(9)


    print("{} from {}".format(nums, line))
    
        

print("sum is: {}".format(sum))