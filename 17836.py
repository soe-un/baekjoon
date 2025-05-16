from collections import deque
import sys
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M, T = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(N)]

gramDist = float("inf")
minRes = float("inf")

def bfs(sx, sy, v):
    global gramDist
    q = deque()
    q.append((sx, sy))
    v[sy][sx] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            ix, iy = x + dx[i], y + dy[i]
            if 0 <= ix < M and 0 <= iy < N and v[iy][ix] == -1:
                if g[iy][ix] == 0:
                    v[iy][ix] = v[y][x] + 1
                    q.append((ix, iy))
                if g[iy][ix] == 2:
                    gramDist = (N-1 - iy) + (M-1 - ix) + v[y][x] + 1
                    v[iy][ix] = v[y][x] + 1
                    q.append((ix, iy))
                if ix == M-1 and iy == N-1:
                    return min(v[y][x] + 1, gramDist)
    return gramDist

v = [[-1 for _ in range(M)] for _ in range(N)]
minRes = bfs(0, 0, v)

print(minRes if minRes <= T else "Fail")
