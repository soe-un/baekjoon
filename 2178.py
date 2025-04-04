from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())

g = []

for _ in range(N):
    g.append(list(map(int, input())))

def dfs(s):
    v=[]
    t=deque()
    t.append(s)
    while t:
        tmp = t.popleft()
        if tmp not in v:
            v.append(tmp)
            for i in range(4):
                ix = tmp[0]+dx[i]
                iy = tmp[1]+dy[i]
                if(ix >= 0 and ix < (M) and iy >= 0 and iy < (N)):
                    if(g[iy][ix] == 1 and (ix, iy) not in v):
                        t.append((ix, iy))
                        g[iy][ix] += g[tmp[1]][tmp[0]]
            
    return g[N-1][M-1]
    

print(dfs((0, 0)))
