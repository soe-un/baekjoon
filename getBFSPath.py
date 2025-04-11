from collections import deque

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

N = 5
M = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

def BFS(s, e):
    er, ec = e
    sr, sc = s
    visited = [[False for _ in range(N)] for _ in range(N)]
    parent = [[None for _ in range(N)] for _ in range(N)]
    q = deque()
    q.append(s)
    while q:
        tr, tc = q.popleft()
        visited[tr][tc] = True
        if tr == er and tc == ec :
            break
        for i in range(4):
            ir = tr + dy[i]
            ic = tc + dx[i]
            if 0<=ir<N and 0<=ic<N:
                if not visited[ir][ic] and M[ir][ic] != 1:
                    q.append((ir, ic))
                    parent[ir][ic] = (tr, tc)
    print('visited')
    for v in visited:
        print(v)

    print('parent')
    for v in parent:
        print(v)
    path = []
    if visited[er][ec]:
        tmpr = er
        tmpc = ec
        while (tmpr, tmpc) != (sr, sc):
            print('while', tmpr, tmpc)
            path.append((tmpr, tmpc))
            tmpr, tmpc = parent[tmpr][tmpc]
    path.reverse()
    return path

print(BFS((0,0), (4,4)))