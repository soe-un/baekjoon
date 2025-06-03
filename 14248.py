import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
S = int(input())

v = [S-1]

def bfs(s):
    global N
    q = deque()
    q.append(s)

    while q:
        t = q.popleft()
        
        l, r = t - A[t], t + A[t]
        if 0 <= l < N and l not in v:
            q.append(l)
            v.append(l)
        if 0 <= r < N and r not in v:
            q.append(r)
            v.append(r)
            

bfs(S-1)
print(len(v))