import sys
input = sys.stdin.readline

R, C = map(int, input().split())
g = [['.' for _ in range(C+2)]]
for _ in range(R):
    g.append(['.'] + list(input().strip()) + ['.'])
g.append(['.' for _ in range(C+2)])


# 인접한 세 칸 또는 네 칸에 바다가 있는 땅은 모두 잠겨버린다
# 인접 == 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

bye = []

for i in range(R+2):
    for j in range(C+2):
        thisTurn = g[i][j]
        if thisTurn == 'X':
            closeSea = 0
            for k in range(4):
                ix, iy = i + dx[k], j + dy[k]
                if g[ix][iy] == '.':
                    closeSea += 1
            if closeSea == 3 or closeSea == 4:
                bye.append([i, j])

for b in bye:
    r, c = b
    g[r][c] = '.'

sR, eR = 10, 0
sC, eC = 10, 0

for r in range(R+2):
    if 'X' in g[r]:
        if sR > r:
            sR = r
        if eR < r:
            eR = r
for c in range(C+2):
    tmp =[row[c] for row in g]
    if 'X' in tmp:
        if sC > c :
            sC = c
        if eC < c :
            eC = c

for i in range(sR, eR+1):
    for j in range(sC, eC+1):
        print(g[i][j], end='')
    print('')

