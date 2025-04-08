# 2초
# 아기 상어 이동 결정법
# 더 이상 먹을 수 있는 물고기가 공간에 없다면,
# 아기 상어는 엄마 상어에게 도움을 요청함 (종료)

# 먹을 수 있는 물고기가 1마리라면,
# 그 물고기를 먹으러 감

# 먹을 수 있는 물고기가 1마리보다 많다면,
# 거리가 가장 가까운 물고기를 먹으러 감
# 거리 = 물고기가 있는 칸으로 이동할 때 지나야하는 칸의 개수의 최솟값
# 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기
# 가장 위에 있는 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기

# 이동 시간은 1초
# 몇 초 동안 엄마 상어에게 도움을 요청하지 않을 수 있을까?
isDebug = False
from collections import deque
import time
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

N = int(input())

space = []
babyShark = []
for i in range(N):
    l = list(map(int, input().split()))
    space.append(l)
    if 9 in l :
        # 처음 아기 상어 크기 2
        si = l.index(9)
        babyShark = [si, i, 2]
        l[si] = 0


def bfs(shark, space):
    sharkX, sharkY, sharkS = shark
    v = set()
    t = deque()
    t.append([sharkX, sharkY, [(sharkX, sharkY)]])
    if isDebug : print('t', t)
    while t:
        if isDebug : time.sleep(1)
        sx, sy, path = t.popleft()
        if isDebug : print('sx, sy, path', sx, sy, path)
        if isDebug : print((sx, sy) not in v)
        if (sx, sy) not in v: 
            v.add((sx, sy))
            for i in range(4):
                ix = sx + dx[i]
                iy = sy + dy[i]
                if 0 <= ix < N and 0 <= iy < N :
                    if (ix, iy) not in v:
                        sV = space[iy][ix]
                        if (sV == sharkS or sV == 0):
                            t.append([ix, iy, path + [(ix, iy)]])
                        elif 0 < sV < sharkS:
                            space[iy][ix] = 0
                            return path + [(ix, iy)]
                        else: continue
    return []

eatFish = 0
t = 0

while True:
    bfsRes = bfs(babyShark, space)
    if isDebug : print(bfsRes)
    lb = len(bfsRes)
    if lb == 0:
        break
    else:
        bx, by = bfsRes[-1]
        t += lb - 1
        eatFish += 1
        bs = babyShark[2]
        if eatFish == bs :
            bs += 1
            eatFish = 0
        babyShark = [bx, by, bs]
        if isDebug: print('babyShark' , babyShark)
    
print(t)