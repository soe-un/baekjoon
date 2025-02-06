# 시간초과 !!! 못풀겠다
import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
dates = list(map(int, input().strip().split()))

start = 1
end = K

while start <= end:
    mid = (start + end) // 2

    coinSum = 0
    for i in range(1, N):
        if mid - (dates[i] - dates[i-1] - 1) >= 0:
            m = mid
            n = mid - (dates[i] - dates[i-1] - 1)
            S = (n + m) * (m - n + 1) // 2
            coinSum += S
        else:
            S = mid * (mid + 1) // 2
            coinSum += S
    coinSum += mid * (mid + 1) // 2

    if(coinSum >= K):
        end = mid - 1
    else :
        start = mid + 1

print(start)


#이건 메모리 초과
import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
dates = list(map(int, input().strip().split()))

start = 1
end = K
res = 0
while start <= end:
    mid = (start + end) // 2
    maxDatesRange = max(dates)
    coinsSum = 0
    curCoinValue = 0
    for i in range(maxDatesRange):
        if((i+1) in dates): 
            curCoinValue = mid
            coinsSum += mid
        else:
            if(curCoinValue > 0):
                curCoinValue -= 1
                coinsSum += curCoinValue

    coinsSum += sum(range(curCoinValue))

    if(coinsSum >= K):
        res = mid
        end = mid - 1
    else :
        start = mid + 1

print(res)