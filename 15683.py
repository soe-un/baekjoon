from collections import deque
isDebug = True

N, M = map(int, input().split())
o = []
for _ in range(N):
    o.append(list(map(int, input().split())))

cctv=[]
for j in range(N):
    for i in range(M):
        if o[j][i] > 0 and o[j][i] != 6 :
            cctv.append((i, j))


def goLeft(p, gg):
    x, y = p
    while x - 1 >= 0:
        target = gg[y][x-1]
        if target == 6:
            break
        elif target > 0:
            x -= 1
            continue
        elif target == 0:
            gg[y][x-1] = '#'
            x -= 1
            continue
        else: x -= 1
    if isDebug: 
        print('goLeft')
        for g in gg:
            print(g)

def goRight(p, gg):
    x, y = p
    while x + 1 < M:
        target = gg[y][x+1]
        if target == 6:
            break
        elif target > 0:
            x += 1
            continue
        elif target == 0:
            gg[y][x+1] = '#'
            x += 1
            continue
        else: x += 1
    if isDebug: 
        print('goRight')
        for g in gg:
            print(g)

def goUp(p, gg):
    x, y = p
    while y - 1 >= 0:
        target = gg[y-1][x]
        if target == 6:
            break
        elif target > 0:
            y -= 1
            continue
        elif target == 0:
            gg[y-1][x] = '#'
            y -= 1
            continue
        else: y -= 1
    if isDebug: 
        print('goUp')
        for g in gg:
            print(g)

def goDown(p, gg):
    x, y = p
    while y + 1 < N:
        target = gg[y+1][x]
        if target == 6:
            break
        elif target > 0:
            y += 1
            continue
        elif target == 0:
            gg[y+1][x] = '#'
            y += 1
            continue
        else: y += 1
    if isDebug: 
        print('goDown')
        for g in gg:
            print(g)

# q = deque()
# while True:
for c in cctv:
    cx, cy = c
    tg = [i for i in o]
    if tg[cx][cy] == 1:
        goLeft(c, tg)
        goRight(c, tg)
        goUp(c, tg)
        goDown(c, tg)
    
