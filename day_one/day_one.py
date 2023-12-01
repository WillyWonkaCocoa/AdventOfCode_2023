f = open('day_1.txt') 
lines = f.readlines()
sum = 0
for line in lines:
    print(line)
    #filter out all non digits
    nums = [x for x in [*line] if x.isdigit()]
    print(nums[0]+nums[-1])
    number = int(nums[0]+nums[-1])
    print(number)
    sum += number

print("sum is: {}".format(sum))