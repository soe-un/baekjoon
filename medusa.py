from collections import deque
isDebug= False

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
sdx = [-1, 1, 0, 0]
sdy = [0, 0, -1, 1]
arrM = []
G = []

N, M = map(int, input().split())
Sr, Sc, Er, Ec = map(int, input().split())
inputM = list(map(int, input().split()))
for _ in range(N):
    G.append(list(map(int, input().split())))

# 입력값 정제
for i in range(0, M*2, 2):
    arrM.append((inputM[i], inputM[i+1]))

# 메두사 시야각에 있는 전사 수 계산
# 상 - 0, 하 - 1, 좌 - 2, 우 - 3
def getMVision(direction, r, c):
    warrior = []
    visionRange = []
    # 검증 방향 저장용 dict
    warriorVision = {0:[], 1:[], 2:[], 3:[],
                     4:[], 5:[], 6:[], 7:[],
                     8:[], 9:[],10:[],11:[]}
    if direction == 0 or direction == 1:
        for y in range(1, N):
            iy = r + (y * dy[direction])
            if 0 <= iy < N:
                for ix in range(c-y, c+y+1):
                    if 0<=ix<N:
                        visionRange.append((iy, ix))
                        if (iy, ix) in arrM:
                            # 나중에 전사 시야각 검증 해야 하므로 좌표 저장
                            warrior.append((iy, ix))
        # 메두사로부터의 시야 방향 계산
        for w in warrior:
            wr, wc = w
            if r < wr : # 아래에 있음
                if c - wc > 0 : # 왼쪽에 있음
                    warriorVision[5].append(w)
                elif c - wc < 0 : # 오른쪽에 있음
                    warriorVision[7].append(w)
                else: # 바로 아래임
                    warriorVision[1].append(w)
            else: # 위에 있음
                if c - wc > 0 : # 왼쪽에 있음
                    warriorVision[4].append(w)
                elif c - wc < 0 : # 오른쪽에 있음
                    warriorVision[6].append(w)
                else: # 바로 위임
                    warriorVision[0].append(w)

    if direction == 2 or direction == 3:
        for x in range(1, N):
            ix = c + (x * dx[direction])
            if 0 <= ix < N:
                for iy in range(r-x, r+x+1):
                    if 0<=iy<N:
                        visionRange.append((iy, ix))
                        if (iy, ix) in arrM:
                            # 나중에 전사 시야각 검증 해야 하므로 좌표 저장
                            warrior.append((iy, ix))
        # 메두사로부터의 시야 방향 계산
        for w in warrior:
            wr, wc = w
            if c > wc : # 전사가 왼쪽에 있음
                if r > wr : # 위에 있음
                    warriorVision[8].append(w)
                elif r < wr : # 아래에 있음
                    warriorVision[10].append(w)
                else: # 바로 왼쪽임
                    warriorVision[2].append(w)
            else: # 오른쪽에 있음
                if r > wr : # 위에 있음
                    warriorVision[9].append(w)
                elif r < wr : # 아래에 있음
                    warriorVision[11].append(w)
                else: # 바로 오른쪽임
                    warriorVision[3].append(w)
    
    # if isDebug:
    #     print('direction', direction)
    #     print('first res: ', warrior, visionRange)

    
    if len(warrior) == 0 :
        return warrior, visionRange
    
    # 전사 시야각에서 보이는 전사들 빼기
    for i in range(12):
        if len(warriorVision[i]) > 0:
            wV = warriorVision[i]
            for w in wV:
                wr, wc = w
                getKVision(i, wr, wc, warrior, visionRange)
    
    # if isDebug:
    #     print('remove safe res: ', warrior)
    #     print('remvoe safe Range', visionRange)

    return warrior, visionRange

# 전사 시야각 계산 검증
# 12시부터 시계방향으로 
# 1사분면: 0 - 6 - 9
# 2사분면: 3 - 11 - 7
# 3사분면: 1 - 5 - 10
# 4사분면: 2 - 8 - 4
def getKVision(direction, r, c, warrior, visionRange):
    if direction in [0, 1, 2, 3]:
        for i in range(1, N):
            ix = c + i * dx[direction]
            iy = r + i * dy[direction]
            if 0<=ix<N and 0<=iy<N and (iy, ix) in visionRange:
                    visionRange.remove((iy, ix))
                    if (iy, ix) in warrior:
                        warrior.remove((iy, ix))
    if direction in [4, 5] :
        for y in range(1, N):
            iy = r + (y * dy[direction-4])
            if 0 <= iy < N:
                for ix in range(c-y, c+1):
                    if 0<=ix <N and (iy, ix) in visionRange:
                        visionRange.remove((iy, ix))
                        if (iy, ix) in warrior:
                            warrior.remove((iy, ix))
    if direction in [6, 7]:
        for y in range(1, N):
            iy = r + (y * dy[direction-6])
            if 0 <= iy < N:
                for ix in range(c, c+y+1):
                    if 0<=ix <N and (iy, ix) in visionRange:
                        visionRange.remove((iy, ix))
                        if (iy, ix) in warrior:
                            warrior.remove((iy, ix))
    if direction in [8, 9]:
        for x in range(1, N):
            ix = c + (x * dx[direction-6])
            if 0 <= ix < N:
                for iy in range(r-x, r+1):
                    if 0<=iy<N and (iy, ix) in visionRange:
                        visionRange.remove((iy, ix))
                        if (iy, ix) in warrior:
                            warrior.remove((iy, ix))
    if direction in [10, 11]:
        for x in range(1, N):
            ix = c + (x * dx[direction-8])
            if 0 <= ix < N:
                for iy in range(r, r+x+1):
                    if 0<=iy<N and (iy, ix) in visionRange:
                        visionRange.remove((iy, ix))
                        if (iy, ix) in warrior:
                            warrior.remove((iy, ix))

# 턴 시작 전에, 메두사가 이동할 경로 지정
def BFS(sr, sc, er, ec):
    q = deque()
    visited = [[False]*N for _ in range(N)]
    parent = [[None]*N for _ in range(N)]
    q.append((sr, sc))
    visited[sr][sc] = True

    while q:
        r, c = q.popleft()
        if (r, c) == (er, ec): break
        for d in range(4):
            nr, nc = r + dy[d], c + dx[d]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and G[nr][nc] == 0:
                visited[nr][nc] = True
                parent[nr][nc] = (r, c)
                q.append((nr, nc))

    # 도착점부터 역추적해서 경로 복원
    if not parent[er][ec]: return []

    path = []
    cur = (er, ec)
    while cur != (sr, sc):
        path.append(cur)
        cur = parent[cur[0]][cur[1]]
    path.reverse()
    return path

def getDistance(sr, sc, er, ec):
    return abs(sr - er) + abs(sc - ec)

pathToPark = BFS(Sr, Sc, Er, Ec)
lptp = len(pathToPark)

if len(pathToPark) == 0 :
    print(-1)

else:
    mp = deque(pathToPark)
    
    while mp:
        # ----- 메두사 이동 -----
        thisTurnMedusaPosition = mp.popleft()
        tmpr, tmpc = thisTurnMedusaPosition

        if tmpr == Er and tmpc == Ec:
            print(0)
            break

        if (tmpr, tmpc) in arrM:
            arrM = [i for i in arrM if i != (tmpr, tmpc)]
            if isDebug: print('filter ',  [i for i in arrM if i != (tmpr, tmpc)])
        
        if isDebug:
            print('now Medusa here', tmpr, tmpc)
            arrM.sort(key=lambda x:x[1])
            arrM.sort(key=lambda x:x[0])
            print('warriors', arrM)

        # ----- 매두사 방향 선정 -----
        maxW = []
        maxStoneCnt = 0
        maxDir = -1
        maxVR = []
        for i in range(4):
            tmpW, tmpVR = getMVision(i, tmpr, tmpc)
            beStoneWCnt = 0
            for arrmele in arrM:
                if arrmele in tmpW:
                    beStoneWCnt += 1
            if beStoneWCnt > maxStoneCnt :
                maxW = tmpW
                maxStoneCnt = beStoneWCnt
                maxDir = i
                maxVR = tmpVR
        if isDebug:
            print('maxDir', maxDir)
            maxW.sort(key=lambda x:x[1])
            maxW.sort(key=lambda x:x[0])
            print('maxW', maxW)
            maxVR.sort(key=lambda x:x[1])
            maxVR.sort(key=lambda x:x[0])
            print('maxVR', maxVR)
        # ----- 전사 이동 -----
        toDeadW = []
        moveCnt = 0
        for i in range(len(arrM)):
            mr, mc = arrM[i]
            if isDebug: print('warrior i', i, mr, mc)
            # --- 돌이 된 전사인지 체크
            if (mr, mc) in maxW :
                continue
            # --- 첫번째 이동, 상하좌우
            minDis = getDistance(mr, mc, tmpr, tmpc)
            minDir = -1
            for j in range(4):
                ir = mr + dy[j]
                ic = mc + dx[j]
                if 0 <= ir < N and 0 <= ic < N and (ir, ic) not in maxVR:
                    iD = getDistance(ir, ic, tmpr, tmpc)
                    if iD < minDis :
                        minDis = iD
                        minDir = j
            if isDebug: print('Warrior Step,', i, mr, mc, minDir, minDis)
            if minDir != -1 :
                moveCnt += 1
                # 이동하려는 위치에 메두사가 있을 때
                if mr + dy[minDir] == tmpr and mc + dx[minDir] == tmpc:
                    toDeadW.append((mr, mc))
                    if isDebug: print("Warrior remove...", toDeadW)
                    continue
                arrM[i] = (mr + dy[minDir], mc + dx[minDir])
                if isDebug: print("First move", arrM[i])
                mr, mc = arrM[i]
                # --- 두번째 이동, 좌우상하 
                minDis = getDistance(mr, mc, tmpr, tmpc)
                minDir = -1
                for j in range(4):
                    ir = mr + sdy[j]
                    ic = mc + sdx[j]
                    if 0 <= ir < N and 0 <= ic < N and (ir, ic) not in maxVR:
                        iD = getDistance(ir, ic, tmpr, tmpc)
                        if isDebug: print('second step cal', j,ir, ic, mr, mc, iD, minDir, minDis)
                        if iD < minDis :
                            minDis = iD
                            minDir = j
                if isDebug: print('Warrior Second Step,', i, mr, mc, minDir, minDis)
                if minDir != -1 :
                    moveCnt += 1
                    # 이동하려는 위치에 메두사가 있을 때
                    if mr + sdy[minDir] == tmpr and mc + sdx[minDir] == tmpc:
                        toDeadW.append((mr, mc))
                        if isDebug: print("Warrior remove at Second", toDeadW)
                        continue
                    arrM[i] = (mr + sdy[minDir], mc + sdx[minDir])
                    if isDebug: print("Second move", arrM[i])
        
        # 사라진 전사 처리
        for t in toDeadW :
            arrM.remove(t)

        # ---- 턴 종료 -----
        # 모든 전사가 이동한 거리의 합
        a = moveCnt
        # 메두사로 인해 돌이 된 전사의 수
        b = maxStoneCnt
        # 메두사를 공격한 전사의 수
        c = len(toDeadW)
        if isDebug: print("***********TURN ENDED**********")
        print(a, b, c)

    

