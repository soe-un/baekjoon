from collections import deque
N, M = map(int, input().split())
g = []
v = []
for n in range(N):
    g.append(list(map(int, input().split())))
    

maxY = range(N)
maxX = range(M)

for j in maxY:
    if 2 in g[j]:
        for i in maxX:
            if g[j][i] == 2: v.append((i, j))
        

res = 0

def goVirus(graph):
    t = deque()
    safeZoneCnt = 0
    for vc in v:
        t.append(vc)
    while t:
        x, y = t.popleft()
        if x + 1 < M and graph[y][x+1] == 0:
            graph[y][x+1] = 2
            if (x+1, y) not in t : t.append((x+1, y))
        if x - 1 >= 0 and graph[y][x-1] == 0:
            graph[y][x-1] = 2
            if (x-1, y) not in t : t.append((x-1, y))
        if y + 1 < N and graph[y+1][x] == 0:
            graph[y+1][x] = 2
            if (x, y+1) not in t : t.append((x, y+1))
        if y - 1 >= 0 and graph[y-1][x] == 0:
            graph[y-1][x] = 2
            if (x, y-1) not in t : t.append((x, y-1))
    
    for gc in graph:
        cnt = 0
        for c in gc:
            if c == 0 : cnt += 1
        safeZoneCnt += cnt
    return safeZoneCnt

for fy in maxY:
    for fx in maxX:
        f = (fx, fy)
        if g[fy][fx] != 0 : continue
        for sy in maxY:
            for sx in maxX:
                s = (sx, sy)
                if f == s : continue
                if g[sy][sx] != 0 : continue
                for ty in maxY:
                    for tx in maxX:
                        t = (tx, ty)
                        if f == t or s == t : continue
                        if g[ty][tx] != 0 : continue
                        tmpG = [[i for i in gc] for gc in g]
                        tmpG[fy][fx] = 1
                        tmpG[sy][sx] = 1
                        tmpG[ty][tx] = 1
                        
                        tR = goVirus(tmpG)
                        if tR >= res : 
                            res = tR

print(res)