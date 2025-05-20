from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
d = dict()

for _ in range(M):
    u, v = map(int, input().split())
    if u in d: d[u].append(v)
    else: d[u] = [v]
    if v in d: d[v].append(u)
    else: d[v] = [u]

cnt = 0
v = []

def findCycle(s):
    q = deque()
    q.append(s)
    v.append(s)
    while q:
        tmp = q.popleft()
        if tmp in d:
            for dt in d[tmp]:
                if dt not in v:
                    q.append(dt)
                    v.append(dt)
    

for i in range(1, N+1):
    if i not in v:
        findCycle(i)
        cnt  += 1

print(cnt)