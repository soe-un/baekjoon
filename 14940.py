import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

input = sys.stdin.readline
N, M = map(int, input().split())
g = []
e = (0, 0)

for _ in range(N):
    iL = list(map(int, input().split()))
    g.append(iL)
    if 2 in iL:
        e = (iL.index(2), _) # x, y


def BFS(s):
    global N, M, g
    v = [[0 for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append(s)
    v[s[1]][s[0]] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            ix, iy = x + dx[i], y + dy[i]
            if 0<= ix < M and 0 <= iy < N:
                if g[iy][ix] == 1 and v[iy][ix] == 0:
                    v[iy][ix] = v[y][x] + 1
                    q.append((ix, iy))
    return v

res = BFS(e)

for i in range(N):
    for j in range(M):
        if (j, i) == e : continue
        if res[i][j] == 0 and g[i][j] == 1:
            res[i][j] = -1

for r in res:
    print(*r)