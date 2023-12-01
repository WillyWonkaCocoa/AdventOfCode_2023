f = open('day_one.txt') 
lines = f.readlines()
sum = 0

for line in lines:
    nums = []
    print(line)

    max_i = len(line) - 1
    for i in range(len(line)):
        if line[i].isdigit():
            nums.append(line[i])
        else:
            if line[i] == 'o': #one +2
                if i + 2 <= max_i and line[i:i+3] == "one":
                    nums.append('1')
            elif line[i] == 't': #two, ten, +2 three +4
                if i + 2 <= max_i and line[i:i+3] == "two":
                    nums.append('2')
                elif i + 4 <= max_i and line[i:i+5] == "three":
                    nums.append('3')
            elif line[i] == 'f': #four, five +3
                if i + 2 <= max_i and line[i:i+4] == "four":
                    nums.append('4')
                elif i + 2 <= max_i and line[i:i+4] == "five":
                    nums.append('5')
            elif line[i] == 's': #six, +2 seven +4
                if i + 2 <= max_i and line[i:i+3] == "six":
                    nums.append('6')
                elif i + 4 <= max_i and line[i:i+5] == "seven":
                    nums.append('7')
            elif line[i] == 'e': #eight +4
                if i + 4 <= max_i and line[i:i+5] == "eight":
                    nums.append('8')
            elif line[i] == 'n': #nine +3
                if i + 3 <= max_i and line[i:i+4] == "nine":
                    nums.append('9')

    print("{} from {} -> {}".format(nums, line, int(nums[0]+nums[-1])))
    sum += int(nums[0]+nums[-1])

print("sum is: {}".format(sum))