# 루돌프 = 반란을 일으켜 선물 배달을 방해하려고 함, 단 한 마리
# how? 산타한테 박치기
# 산타 = 크리스마스를 구해야 함, P명
# how? 루돌프를 잡음
isDebug = True
# 산타 P명 
# 게임판 N x N, (r, c), 1부터 시작, r이 행(y)
# M은 턴 수, C는 루돌프 힘, D는 산타 힘
N, M, P, C, D = map(int, input().split())
Rr, Rc = map(int, input().split())
Rr, Rc = Rr - 1, Rc - 1

# 게임판
board = [[0 for i in range(N)] for j in range(N)]
board[Rr][Rc] = 50 # 루돌프는 칸에서 50!

S = dict()
santaScore = dict()
for _ in range(P):
    pn, sr, sc = list(map(int, input().split()))
    S[pn] = (sr-1, sc-1)
    santaScore[pn] = 0
    board[sr-1][sc-1] = pn

# 산타 번호 범위
santaRange = range(1, P+1)

# 0은 활성화, -1은 탈락, 1은 기절
status = [0 for _ in range(P+1)]

if isDebug:
    print('init')
    print('N, M, P, C, D', N, M, P, C, D)
    print('board')
    for b in board:
        print(b)
    print('status', status)

def getDistance(a, b):
    # 거리는 (r1 - r2)^2 + (c1 - c2)^2
    ar, ac = a
    br, bc = b
    return (ar-br) ** 2 + (ac-bc) ** 2

# 루돌프 이동 가능 방향: 12시부터 시계방향으로
drx = [0, 1, 1, 1, 0, -1, -1, -1]
dry = [-1, -1, 0, 1, 1, 1, 0, -1]

# 산타 이동 가능 방향: 우선순위 역순, 좌=0하=1우=2상=3
dsx = [-1, 0, 1, 0]
dsy = [0, 1, 0, -1]

isGameOver = False

# 충돌 이후 포물선으로 이동한 칸에 산타가 있다면(상호작용)
# 1. 기존에 있던 산타는 포물선과 동일한 방향으로 1칸 밀려남
# 2. 밀려난 위치에 산타가 있다면 연쇄적으로 밀려남
# 3. 밀려난 산타가 게임판 밖으로 가면 게임에서 탈락
# 3-1. 모든 산타가 탈락이라면 즉시 게임 종료
def goInteraction(crashSanta, nowR, nowC, dr, dc):
    global N, M, P, C, D, Rr, Rc, board, S, santaScore, santaRange, status, drx, dry, dsx, dsy, isGameOver
    interactionSanta = board[nowR][nowC]
    board[nowR][nowC] = crashSanta
    iSr, iSc = S[interactionSanta]
    idr, idc = iSr + dr, iSc + dc
    if 0 <= idr < N and 0 <= idc < N :
        # 2-2. 밀려난 칸에 다른 산타가 있다면 상호작용
        if board[idr][idc]:
            goInteraction(interactionSanta, idr, idc, dr, dc)
        else:
            S[interactionSanta] = (idr, idc)
            board[iSr][iSc] = 0
            board[idr][idc] = interactionSanta
    else:
        # 2-1. 밀려난 위치가 게임판 밖이라면 산타는 탈락
        status[interactionSanta] = -1
        # 2-1-1. 모든 산타가 탈락이라면 즉시 게임 종료
        if status.count(-1) == P :
            isGameOver = True

# 루돌프가 움직이는 방식
def moveRudolph():
    global N, M, P, C, D, Rr, Rc, board, S, santaScore, santaRange, status, drx, dry, dsx, dsy, isGameOver
    # 1. 가장 가까운 산타를 찾음
    distSanta = dict()
    for i in santaRange:
        if i in S and status[i] != -1:
            distI = getDistance((Rr, Rc), S[i])
            if distI in distSanta:
                distSanta[distI].append(S[i])
            else:
                distSanta[distI] = [S[i]]
    closeDist = min(distSanta.keys())
    # 1-1. 거리가 가까운 산타가 1명이면 그 산타 위치 구하기
    destination = []
    if len(distSanta[closeDist]) == 1:
        destination = distSanta[closeDist][0]
    else:
        # 1-2. 2명 이상이면, r이 큰 산타 위치,
        # 1-3. r이 동일하면, c가 큰 산타 위치 구하기
        distSanta[closeDist].sort(key=lambda x:x[1], reverse=True)
        distSanta[closeDist].sort(key=lambda x:x[0], reverse=True)
        destination = distSanta[closeDist][0]
    # 2. 위치와 가까운 방향 찾기
    # * 돌진 시 방향은 8방향(대각선 포함)
    # * 돌진하는 칸은 8방향 중 가장 가까워지는 방향
    distWhenGo = [0 for _ in range(8)] # 12시 부터 시계방향
    directionWhenGo = 0
    # 2-1. 모든 칸을 향해 한 칸 돌진헸을 때 목적지와의 거리 저장
    for i in range(8):
        distWhenGo[i] = getDistance(destination, (Rr+dry[i], Rc+drx[i]))
    if isDebug : 
            print('Rudolph distWhenGo', distWhenGo)
    directionWhenGo = distWhenGo.index(min(distWhenGo))


    # 3. 돌진하기
    toGoRr, toGoRc = Rr+dry[directionWhenGo], Rc+drx[directionWhenGo]
    toGoVlaue = board[toGoRr][toGoRc]
    # 3-1. 돌진한 칸에 산타가 없으면 그냥 보드 정리하고 리턴
    if toGoVlaue == 0 :
        board[toGoRr][toGoRc] = 50
        board[Rr][Rc] = 0
        Rr, Rc = toGoRr, toGoRc
        return
    # 3-2. 산타가 있으면 충돌 로직 정리
    else: 
        # 충돌 당한 산타는 한 턴 기절함
        status[toGoVlaue] = 1
        # 1. 해당 산타는 C만큼의 점수를 얻음
        santaScore[toGoVlaue] += C
        # 2. 산타는 루돌프가 이동해온 방향으로 C칸만큼 밀려남
        dr, dc = toGoRr + (dry[directionWhenGo]*C) , toGoRc + (drx[directionWhenGo]*C)
        if 0 <= toGoRr < N and 0 <= dc < N :
            # 2-2. 밀려난 칸에 다른 산타가 있다면 상호작용
            if board[dr][dc] > 0:
                directionWhenGo[toGoRr][toGoRc] = 50
                goInteraction(toGoVlaue, dr, dc, dry[directionWhenGo], drx[directionWhenGo])
            else:
                S[toGoVlaue] = (dr, dc)
                board[toGoRr][toGoRc] = 50
                board[dr][dc] = toGoVlaue
        else:
            # 2-1. 밀려난 위치가 게임판 밖이라면 산타는 탈락
            board[toGoRr][toGoRc] = 50
            status[toGoVlaue] = -1
            # 2-1-1. 모든 산타가 탈락이라면 즉시 게임 종료
            if status.count(-1) == P :
                isGameOver = True
    return


# 산타가 움직이는 방식
def moveSanta():
    global N, M, P, C, D, Rr, Rc, board, S, santaScore, santaRange, status, drx, dry, dsx, dsy, isGameOver
    # range(1, P+1) 순서대로
    for i in santaRange:
        # 1. 산타의 현재 상황 체크: 기절했거나 탈락한 산타면 패스
        if status[i] != 0 :
            continue

        # 2. 루돌프와 가까워지는 방법 체크
        sr, sc = S[i]
        nowDist = getDistance((Rr, Rc), (sr, sc))
        # * 이동 시 방향은 4방향, 우선순위는 상우하좌 (순서는 거꾸로 만듦)
        distWhenGo = [-1 for _ in range(4)] # 좌하우상
        directionWhenGo = -1

        # 2-1. 산타를 상, 우, 하, 좌로 움직였을 때 케이스 순회
        for moveI in range(4):
            ir, ic = sr + dsy[moveI], sc + dsx[moveI]
            # 2-1-1. 움직인 위치가 게임판 안인지 확인
            if (0 <= ir < N) and (0<= ic < N):
                # 2-1-2. 움직인 위치에 다른 산타가 있는지 확인
                if board[ir][ic] == 2:
                    continue
                else:
                    # 2-2. 목적지와의 거리&방향 저장
                    iDist = getDistance((Rr, Rc), (ir, ic))
                    distWhenGo[moveI] = iDist
    
        # directionWhenGo를 우선순위대로 지정
        minDist = 2*N**N + 1
        for mi in range(4):
            minI = distWhenGo[mi]
            if minI != -1 and minI <= minDist:
                directionWhenGo = mi
                minDist = minI
        if isDebug: print('nowDist, distWhenGo, directionWhenGo', nowDist, distWhenGo, directionWhenGo)
        # 2-2-1. 모든 방향에서 가까워질 수 없다면 이동 패스
        if directionWhenGo == -1 : continue

        # 3. 루돌프에게 거리가 가장 가까워지는 방향으로 1칸 이동
        toGoSr, toGoSc = sr + dsy[directionWhenGo], sc + dsx[directionWhenGo]
        toGoValue = board[toGoSr][toGoSc]
        if isDebug:
            print('Santa Step 3.', toGoValue, directionWhenGo,  toGoSr, toGoSc)
        # 산타가 움직인 칸에 루돌프가 있다면 ...
        if toGoValue == 50:
            # 충돌 당한 산타는 한 턴 기절함
            cSr, cSc = S[i]
            status[i] = 1
            # 1. 해당 산타는 D만큼의 점수를 얻음
            santaScore[i] += D
            # 2. 산타는 자신이 이동해온 반대 방향으로 D칸만큼 밀려남
            dr, dc = cSr - (dsy[directionWhenGo]*D) , cSc - (dsx[directionWhenGo]*D)
            if 0 <= dr < N and 0 <= dc < N :
                # 2-2. 밀려난 칸에 다른 산타가 있다면 상호작용
                if board[dr][dc] > 0:
                    board[toGoSr][toGoSc] = i
                    goInteraction(toGoValue, dr, dc, dsy[directionWhenGo], dsx[directionWhenGo])
                else:
                    S[i] = (dr, dc)
                    board[cSr][cSc] = 0
                    board[dr][dc] = i
            else:
                # 2-1. 밀려난 위치가 게임판 밖이라면 산타는 탈락
                board[sr][sc] = 0
                status[i] = -1
                # 2-1-1. 모든 산타가 탈락이라면 즉시 게임 종료
                if isDebug: print('status.count(-1)', status.count(-1))
                if status.count(-1) == P :
                    isGameOver = True

            if isGameOver : break
        else:
            board[sr][sc] = 0
            S[i] = (toGoSr, toGoSc)
            board[toGoSr][toGoSc] = i
    return


# 턴 M번
for m in range(M):
    if isDebug: print('-----Turn m-----', m)
    # 기절한 산타 턴 체크
    for i in santaRange:
        if status[i] == 1: status[i] -= 1

    # 턴마다 루돌프들이 한 번 움직이고
    moveRudolph()
    if isGameOver : break
    # 산타는 1~P번까지 순서대로 (range(1, P+1)) 한 번 씩 움직임
    moveSanta()
    if isGameOver : break
    
    # 턴 종료 후 탈락하지 않는 산타는 1점 추가 부여
    for di in santaRange:
        if status[di] >= 0 : santaScore[di] += 1
    if isDebug:
        print('*****---TURN M RES----*****', m)
        print('board')
        for b in board:
            print(b)
        print('staus', status)


# 각 산타가 얻은 최종 점수 출력 (1번부터 P번까지 공백을 사이에 두고 출력)
for pi in santaRange:
    print(santaScore[pi], end=' ')















