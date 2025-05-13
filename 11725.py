from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

p = [0 for _ in range(N+1)]

d = dict()
for _ in range(N-1):
    tmp = list(map(int, input().split()))
    if tmp[0] in d: d[tmp[0]].append(tmp[1])
    else: d[tmp[0]] = [tmp[1]]
    if tmp[1] in d: d[tmp[1]].append(tmp[0])
    else: d[tmp[1]] = [tmp[0]]


def BFS(s):
    q= deque()
    q.append(s)

    while q:
        t = q.popleft()
        for i in d[t]:
            if i != 1 and p[i] == 0 :
                p[i] = t
                q.append(i)
                d[i].remove(t)



BFS(1)
for i in range(2, N+1):
    print(p[i])