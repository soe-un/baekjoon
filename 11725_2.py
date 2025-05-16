from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
d = dict()

for _ in range(N-1):
    s, e = map(int, input().split())
    if s in d : d[s].append(e)
    else: d[s] = [e]
    if e in d : d[e].append(s)
    else: d[e] = [s]

res = [0 for _ in range(N+1)]

def DFS(s):
    v = [False for _ in range(N + 1)]
    q = deque()
    q.append(s)
    while q:
        tmp = q.pop()
        v[tmp] = True
        for i in d[tmp]:
            if not v[i]:
                res[i] = tmp
                q.append(i)
                d[i].remove(tmp)
DFS(1)
print(*res[2:])

