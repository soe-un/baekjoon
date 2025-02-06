import sys
input = sys.stdin.readline

N, C = map(int, input().strip().split())
house = list(int(input().strip()) for _ in range(N))
house.sort()

start, end = 1, house[-1] - house[0]
res = 0

while start <= end :
    mid = (start + end) // 2
    current = house[0]
    count = 1

    for i in range(1, len(house)):
        if house[i] >= current + mid:
            count += 1
            current = house[i]
    if count >= C:
        start = mid + 1
        res = mid
    else:
        end = mid -1

print(res)
        

