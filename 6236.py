import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
P = [int(input().strip()) for _ in range(N)]

startM, endM = max(P), sum(P)

while startM <= endM:
    mid = (startM + endM) // 2
    charge = mid
    cnt = 1
    for i in P:
        if(charge - i) < 0 : #부족해잉
            cnt += 1
            charge = mid
        charge -= i
    if cnt > M: #K가 너무 작앙
        startM = mid + 1
    else: # K가 너무 컹
        endM = mid - 1

print(mid)