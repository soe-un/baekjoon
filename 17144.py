from collections import deque
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
q = deque()
isDebug = False
R, C, T = map(int, input().split())
home = []
a = []
for i in range(R):
    l = list(map(int, input().split()))
    home.append(l)
    if -1 in l : a.append(i)


def spreadDirst():
    qh = [[i for i in h] for h in home]
    while q:
        x, y = q.pop()
        for i in range(4):
            ix = x + dx[i]
            iy = y + dy[i]
            if 0 <= ix < C and 0 <= iy < R:
                if home[iy][ix] != -1:
                    mount = int(qh[y][x] / 5)
                    home[iy][ix] += mount
                    home[y][x] -= mount

def circleTop():
    aT = a[0]
    downRange = range(aT-2, -1, -1)
    leftRange = range(1, C)
    upRange = range(1, aT+1)
    rightRange = range(C-2, 0, -1)

    if isDebug:
        print('aT', aT)
        print('Down', list(range(aT-2, -1, -1)))
        print('Left', list(range(1, C)))
        print('Up', list(range(1, aT+1)))
        print('Right', list(range(C-2, 0, -1)))
    
    for d in downRange:
        home[d+1][0] = home[d][0]
    for l in leftRange:
        home[0][l-1] = home[0][l]
    for u in upRange:
        home[u-1][C-1] = home[u][C-1]
    for r in rightRange:
        home[aT][r+1] = home[aT][r]
    home[aT][1] = 0

def circleBottom():
    aB = a[1]
    
    upRange = range(aB+2, R)
    leftRange = range(1, C)
    downRange = range(R-2, aB-1, -1)
    rightRange = range(C-2, 0, -1)

    if isDebug:
        print('aB', aB)
        print('upRange', list(upRange))
        print('leftRange', list(leftRange))
        print('downRange', list(downRange))
        print('rightRange', list(rightRange))
    


    for u in upRange:
        home[u-1][0] = home[u][0]
    for l in leftRange:
        home[R-1][l-1] = home[R-1][l]
    for d in downRange:
        home[d+1][C-1] = home[d][C-1]
    for r in rightRange:
        home[aB][r+1] = home[aB][r]
    
    home[aB][1] = 0


def oneSecond():
    for i in range(R):
        for j in range(C):
            if home[i][j] > 0 :
                q.append((j, i))
    # 미세먼지 확산
    spreadDirst()
    # 공기청정기 작동
    circleTop()
    circleBottom()

for t in range(T):
    oneSecond()

res = 2
for h in home:
    res += sum(h)
print(res)