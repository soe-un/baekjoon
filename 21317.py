import sys
import math

input = sys.stdin.readline
INF = math.inf
N = int(input())
energy = [[]] + [list(map(int,input().split())) for _ in range(N-1)]
K = int(input())
dp = [[INF,INF] for _ in range(N+1)]
dp[1][0] = 0
dp[1][1] = 0
for i in range(2,N+1):
    #작은 점프
    dp[i][0] = min(dp[i][0], dp[i-1][0]+energy[i-1][0])
    dp[i][1] = min(dp[i][1], dp[i-1][1]+energy[i-1][0])
    #큰 점프
    if i-2 > 0:
        dp[i][0] = min(dp[i][0], dp[i-2][0]+energy[i-2][1])
        dp[i][1] = min(dp[i][1], dp[i-2][1]+energy[i-2][1])
    #매우 큰 점프
    if i-3 > 0:
        dp[i][1] = min(dp[i][1], dp[i-3][0]+K)

print(min(dp[N]))