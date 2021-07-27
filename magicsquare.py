# solutoin #1.
possibilities = [
    [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
    [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
    [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
    [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
    [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
    [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
    [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
    [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
]

s = []
for i in range(3):
    s.append([int(x) for x in input().split(' ')])

min_cost = None
for p in possibilities:
    cost = 0
    for i in range(3):
        for j in range(3):
            cost += abs(p[i][j] - s[i][j])
    if min_cost is None or cost < min_cost:
        min_cost = cost
print(min_cost)

# solutoin #2.
input_nums = []
input_nums.extend([int(i) for i in input().split()])
input_nums.extend([int(i) for i in input().split()])
input_nums.extend([int(i) for i in input().split()])

#input_nums[0], input_nums[1], input_nums[2] = [int(i) for i in input().split()]
#input_nums[3], input_nums[4], input_nums[5] = [int(i) for i in input().split()]
#input_nums[6], input_nums[7], input_nums[8] = [int(i) for i in input().split()]
#print(input_nums)

pos = []
pos.append([8,1,6,3,5,7,4,9,2])
pos.append([6,1,8,7,5,3,2,9,4])
pos.append([4,9,2,3,5,7,8,1,6])
pos.append([2,9,4,7,5,3,6,1,8])
pos.append([8,3,4,1,5,9,6,7,2])
pos.append([4,3,8,9,5,1,2,7,6])
pos.append([6,7,2,1,5,9,8,3,4])
pos.append([2,7,6,9,5,1,4,3,8])

#print(pos)

mindiff = 10000

for arr in pos:
    diff = 0
    for i in range(9):
        diff += abs(arr[i] - input_nums[i])
    if (diff < mindiff):
        mindiff = diff
        
print(mindiff)

# Solution #3.
import itertools
s = []
for i in range(3):
    s.extend(list(map(int, input().split(" "))))

min_cost = 1000
best = None
def is_magic(s):
    for i in range(3):
        if sum(s[i*3:i*3+3]) != 15:
            return False
        if sum(s[i::3]) != 15:
            return False
    if s[0] + s[4] + s[8] != 15:
        return False
    if s[2] + s[4] + s[6] != 15:
        return False
    return True

best = None
for p in itertools.permutations(range(1,10)):
    cost = sum([abs(p[i] - s[i]) for i in range(len(s))])
    if cost < min_cost and is_magic(p):
        min_cost = cost
        best = p
        
print(min_cost)
    