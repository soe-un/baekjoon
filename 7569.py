import sys
from collections import deque

r_line = sys.stdin.readline

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


M, N, H = map(int, r_line().split())

boxes = []

for i in range(H):
    b = []
    for j in range(N):
        b.append(list(map(int, r_line().split())))
    boxes.append(b)

t = deque()

def bfs() :
    while t:
        x, y, z = t.popleft()
        for i in range(6):
            ix = x + dx[i]
            iy = y + dy[i]
            iz = z + dz[i]

            if (ix >= 0 and ix < M) and (
                iy >= 0 and iy < N) and (
                    iz >= 0 and iz < H):
                if boxes[iz][iy][ix] == 0:
                    t.append((ix, iy, iz))
                    boxes[iz][iy][ix] = boxes[z][y][x] + 1

for k in range(H):
    for j in range(N):
        for i in range(M):
            if boxes[k][j][i] == 1:
                t.append((i, j, k))

bfs()

maxV = 0
failed = False
notOnlyOne = False

for box in boxes:
    for b in box:

        if 0 in b:
            failed = True
            break

        if 2 in b:
            notOnlyOne = True

        maxB = max(b)
        if maxV <= maxB:
            maxV = maxB
    if failed : break

if failed: print(-1)
elif not notOnlyOne: print(0)
else: print(maxV-1)
