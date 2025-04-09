# combination + BFS
isDebug = False
from collections import deque
from itertools import combinations

N, M = map(int, input().split())
L = []
V = set()
for _ in range(N):
    L.append(list(map(int, input().split())))

cntZero = 0
for y in range(N):
    cntZero += L[y].count(0)
    for x in range(N):
        i = L[y][x]
        if i == 2 :
            V.add((x, y))
            L[y][x] = 0
        elif i == 1:
            L[y][x] = -1

if cntZero == 0:
    print(0)
else:
    res = []
    caseC = list(combinations(V, M))
    if isDebug:
        print('V', V)
        print('caseC', caseC)


    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def bfs(g, v, a):
        global res
        graph = [[i for i in j] for j in g]
        q = deque()
        for vi in v:
            q.append(vi)

        while q:
            tx, ty = q.popleft()
            # if isDebug: print('q', tx, ty)

            for i in range(4):
                ix = tx + dx[i]
                iy = ty + dy[i]
                if 0<=ix<N and 0<=iy<N and graph[iy][ix] == 0 and (ix, iy) not in v:
                    q.append((ix, iy))
                    tmp = graph[ty][tx] + 1
                    # if len(res) >= 1 and min(res) < tmp: return -1
                    graph[iy][ix] += tmp
        for ac in a:
            ax, ay = ac
            graph[ay][ax] = -1

        maxGc = -1
        if isDebug:
            print('graph')
            for g in graph:
                print(g) 
        
        for i in range(N):
            for j in range(N):
                mg = graph[i][j]
                if (j, i) not in v:
                    if mg == 0: return -1
                    if mg >= maxGc: maxGc = mg
        return maxGc

    for c in caseC:
        if isDebug : print('c', c)
        A = V - set(c)
        r = bfs(L, c, A)
        if r >= 0 : res.append(r)

    if len(res) == 0 : print(-1)
    else: print(min(res))
