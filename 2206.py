# 우선은 BFS로 그래프 내부를 1씩 더해가며 경로를 세면 될 것 같은데,
# 벽 부수기 로직이 고민
# -> 모든 벽을 한번씩 0으로 바꿔본다

from collections import deque

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

N, M = map(int, input().split())
g = []
w = []
for j in range(N):
    l = list(map(int, input()))
    for i in range(M):
        if l[i] == 1:
            l[i] = -1 # 횟수를 더해줄 것이기 때문에 벽은 -1로
            w.append((i, j)) # 벽 정보 더해주기
    g.append(l)

def bfs(bg) :
    t = deque()
    t.append((0, 0))

    while t:
        x, y = t.popleft()
        for i in range(4):
            ix = x + dx[i]
            iy = y + dy[i]
            if 0 <= ix < M and 0 <= iy < N and bg[iy][ix] == 0:
                t.append((ix, iy))
                bg[iy][ix] = bg[y][x] + 1

findRoute = False
minV = 1000*1000
for wx, wy in w:
    tg = [[0 for _ in range(M)] for _ in range(N)]
    for j in range(N):
        for i in range(M):
            tg[j][i] = g[j][i]
    tg[wy][wx] = 0

    bfs(tg)
    

    thisV = tg[N-1][M-1]
    if(thisV > 0):
        findRoute = True
        if minV > thisV: minV = thisV


if not findRoute : print(-1)
else: print(minV+1)