import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def findCylce(s, v, g):
    q = deque()
    q.append(s)
    while q:
        tmp = q.pop()
        v.append(tmp)
        if g[tmp] not in v:
            q.append(g[tmp])
        else:
            break

for t in range(T):
    v = []
    d = dict()
    N = int(input())
    l = list(map(int, input().split()))
    cycle = 0
    for i in range(0, N):
        d[i+1] = l[i]

    for i in range(1, N+1):
        if i not in v:
            findCylce(i, v, d)
            cycle += 1
    print(cycle)