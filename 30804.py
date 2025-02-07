from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input().strip())
f = list(map(int, input().strip().split()))

l, r, count = 0, 0, 0

infos = defaultdict(int)
answer = 0
while r < N:
    if infos[f[r]] == 0:
        count += 1
    infos[f[r]] += 1

    while count >2:
        infos[f[l]] -= 1
        if infos[f[l]] == 0:
            count -= 1
        l += 1
    
    answer = max(answer, r-l+1)
    r+= 1

print(answer)