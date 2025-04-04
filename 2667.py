from collections import deque

dx=[1, 0, 0, -1]
dy=[0, 1, -1, 0]

N = int(input())
town = []

rN = range(N)

for _ in rN:
    town.append(list(map(int, input())))

groups = []

def dfs(s):
    v=[]
    t=deque()
    t.append(s)

    groupsNum = len(groups) + 1

    while t:
        tmp = t.pop()
        if(tmp not in v):
            v.append(tmp)
            town[tmp[1]][tmp[0]] += groupsNum
            for i in range(4):
                ix = tmp[0] + dx[i]
                iy = tmp[1] + dy[i]
                if ix >= 0 and ix < N and iy >= 0 and iy < N:
                    if town[iy][ix] == 1 and (ix, iy) not in v:
                        t.append((ix, iy))

    return len(v)

for y in rN:
    for x in rN:
        if town[y][x] == 1:
            
            groups.append(dfs((x, y)))

print(len(groups))
groups.sort()
for g in groups:
    print(g)
