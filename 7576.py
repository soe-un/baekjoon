from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# 2 <= M, N <= 1,000
M, N = map(int, input().split())
box = []
for _ in range(N):
    box.append(list(map(int, input().split())))

toGo = deque()

def bfs():
    global box
    while toGo:
        x, y= toGo.popleft()
        
        for i in range(4):
            ix = x + dx[i]
            iy = y + dy[i]
            if 0<=ix<M and 0<=iy<N and box[iy][ix] == 0:
                toGo.append((ix, iy))
                box[iy][ix] = box[y][x] + 1

        

for i in range(N):
    for j in range(M):
        if(box[i][j] == 1):
            toGo.append((j, i))

bfs()

maxB = 0
allComp = True
for b in box:
    if maxB <= max(b): maxB = max(b)
    if 0 in b:
        allComp = False
        break

if not allComp: print(-1)
else: print(maxB-1)