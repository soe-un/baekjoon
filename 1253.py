import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().strip().split()))
nums.sort()

goodNums = 0
for i in range(N):
    goal = nums[i]
    
    start = 0
    end = len(nums)-1

    while start < end:
        if nums[start] + nums[end] == goal:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                goodNums += 1
                break
        elif nums[start] + nums[end] > goal:
            end -= 1
        elif nums[start] + nums[end] < goal:
            start += 1

print(goodNums)



