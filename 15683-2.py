import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


direction = [
    [], [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]

N, M = map(int, input().split())
g = []
cctv = []
for i in range(N):
    d = list(map(int, input().split()))
    g.append(d)
    for j in range(M):
        if d[j] in [1, 2, 3, 4, 5]:
            cctv.append([d[j], i, j])

def fill(graph, m, x, y):
    for i in m:
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if 0 <= nx < N and 0 <= ny < M :
                if graph[nx][ny] == 6: break
                elif graph[nx][ny] == 0 : graph[nx][ny] = -1
            else: break

def dfs(depth, board):
    global min_v
    if depth == len(cctv):
        cnt = 0
        for i in range(N):
            cnt += board[i].count(0)
        min_v = min(min_v, cnt)
        return

    boardCopy = [[j for j in board[i]] for i in range(N)]
    cctvM, cx, cy = cctv[depth]
    for i in direction[cctvM]:
        fill(boardCopy, i, cx, cy)
        dfs(depth+1, boardCopy)
        boardCopy = [[j for j in board[i]] for i in range(N)]


min_v = int(1e9)
dfs(0, g)
print(min_v)



