import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
T = [int(input().strip()) for _ in range(N)]
T.sort()

start = 1
end = max(T) * M
res = end

while start <= end:
    mid = (end + start) // 2
    passedM = 0
    curT = 0
    for t in T:
        if( t * (mid // t) < curT):
            curT = t * (mid // t)
            passedM += (mid // t)
        else:
            passedM += (mid // t)

    if(passedM >= M) :
        res = mid
        end = mid - 1
    elif(passedM < M):
        start = mid + 1

print(res)