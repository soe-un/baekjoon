from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
m = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    m[b].append(a)

def BFS(s):
    v = [0] * (N+1)
    q = deque([s])
    v[s] = 1
    cnt = 0
    while q:
        tmp = q.popleft()
        cnt += 1
        for i in m[tmp]:
            if not v[i]:
                q.append(i)
                v[i] = 1
    return cnt

bfsRes = [0] * (N + 1)
for i in range(1, N+1):
    bfsRes[i] = BFS(i)

maxCnt = max(bfsRes)

ans = [i for i in range(1, N+1) if bfsRes[i] == maxCnt]

print(*ans)