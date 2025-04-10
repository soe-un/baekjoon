isDebug = False
from collections import deque
import time
L, N, Q = map(int, input().split())
chess = []
K = dict()
Qs = []
dam = dict()
for _ in range(L):
    # L x L 체스판 (1, 1)부터 시작
    # 칸은 0 = 빈칸, 1 = 함정, 또는 2 = 벽
    # 마력으로 상대방을 밀쳐낼 수 있음
    chess.append(list(map(int, input().split())))

for i in range(N):
    # 입력 순서: r, c, h, w, k
    # 기사의 초기 위치는 r,c , 체력은 k
    # 방패를 들고 있어 r, c를 좌측 상단으로 하여 h x w 형태의 직사각형.
    # 기사의 형태는
    # (r, c)   ~ (r+w, c)
    # (r, c+h) ~ (r+w, c+h)
    # 좌표로는 chess[c:c+h-1][r:r+w-1]
    # r, c는 입력 받은 값에서 항상 1을 빼야 함을 유의할 것
    K[i+1] = list(map(int, input().split()))
    dam[i+1] = K[i+1][4]

for _ in range(Q):
    # 입력 순서: i, d
    # i번 기사에게 d 로 한 칸 이동하라는 명령
    # d = 0=위, 1=오른쪽, 2=아래쪽, 3=왼쪽
    # i는 그대로 써도 됨 (dict 사용)
    Qs.append(list(map(int, input().split())))

dc = [0, 1, 0, -1]
dr = [-1, 0, 1, 0]

# 기사들이 받은 대미지 계산용 배열
d = [0 for _ in range(N+1)]
# 탈락한 기사 모음
bye = []

def DFS(s, d):
    global K
    t = deque()
    t.append(s)
    dK = dict()
    # 이동하려는 위치에 다른 기사가 있다면
    # -> 그 기사도 함께 연쇄적으로 한 칸 밀려남
    # ... 그 옆에 또 기사가 있다면 연쇄적으로 한 칸 씩 밀림
    # 그러나 연쇄적으로 밀린 결과 끝에 벽이 있다면, 이동은 없던 일이 됨
    while t:
        ti, tr, tc, th, tw, tk = t.pop()
        # 좌표 계산을 위해 1을 빼줌
        tr, tc = tr-1, tc-1 
        # if isDebug:
        #     time.sleep(1)
        #     print('ti, tr, tc, th, tw, tk', ti, tr, tc, th, tw, tk)
        #     print('dK', dK)
        # 이동 시 체크!
        ics, ice = tc + dc[d], tc+tw + dc[d]
        irs, ire = tr + dr[d], tr+th + dr[d]
        if isDebug: 
            print('pop!')
            print('ics, ice', ics, ice)
            print('irs, ire', irs, ire)

        if 0 <= irs < L and 0 < ire <= L and 0 <= ics < L and 0 < ice <= L:
            hamjung = 0
            # 이동 영역 내부에 벽 또는 함정이 있는지
            for i in range(irs, ire):
                # if isDebug: print('i, chess[i][ics:ice]', i, chess[i][ics:ice])
                if 2 in chess[i][ics:ice]:
                    if isDebug: print('meet wall')
                    return dict()
                if 1 in chess[i][ics:ice]:
                    hamjung += chess[i][ics:ice].count(1)
            dK[ti] = [tr + dr[d] + 1, tc + dc[d] + 1, th, tw, tk-hamjung]
            moveS = set()
            for mr in range(irs, ire):
                for mc in range(ics, ice):
                        moveS.add((mr, mc))

            for i in range(1, N+1):
                if isDebug: print('i', i)
                if ti == i : 
                    # if isDebug: print('its meee', ti)
                    continue
                if i in dK.keys(): 
                    # if isDebug: print('already moved', dK.keys())
                    continue
                if i in K:
                    ar, ac, ah, aw, ak = K[i]
                    ar, ac = ar -1, ac -1
                    # if isDebug: print('ar, ac, ah, aw, ak', ar, ac, ah, aw, ak)
                    ars, are = ar, ar+ah
                    acs, ace = ac, ac+aw
                    aS = set()
                    for kr in range(ars, are):
                        for kc in range(acs, ace):
                            aS.add((kr, kc))
                    if isDebug: 
                        # print('moveS', moveS)
                        # print('aS', aS)
                        print('moveS.intersection(aS)', moveS.intersection(aS))
                    if len(moveS.intersection(aS)) > 0:
                        t.append([i, ar+1, ac+1, ah, aw, ak])
        else : 
            dK = dict()
            if isDebug: print('meet wall')
            break
    # 만약 이동이 성공했다면, 아래 대미지를 계산함
    # 2. 대결 대미지
    # 명령을 받은 기사가 다른 기사를 밀치게 되면, 밀려난 기사는 피해를 입음
    # 명령을 받은 기사는 피해를 입지 않음
    # 이때 각 기사들은
    # 해당 기사가 이동한 곳에서 w x h 직사각형 내에
    # 놓여 있는 함정의 수만큼만 피해를 입음
    # (밀쳐진 위치에 함정이 전혀 없다면, 그 기사는 피해를 전혀 입지 않게 됨)
    # 각 기사마다 피해를 받은 만큼 체력이 깎이게 됨
    
    if s[0] in dK and s[5] != dK[s[0]][4]:
        dK[s[0]][4] = s[5]

    return dK

# 1. 기사 이동
# 왕에게 명령을 받은 기사는 상하좌우 중 하나로 한 칸 이동할 수 있음
def moveK(i, d):
    global chess, K
    # 체스판에서 사라진 기사에게 명령을 내리면 아무 반응이 없음
    if i in bye : return
    # 하나씩 이동해봐서, 이동할 수 있는지 체크
    ir, ic, ih, iw, ik = K[i]
    dK = DFS([i, ir, ic, ih, iw, ik], d)
    if isDebug : 
        print('***at moveK: dK***', dK)
        print(len(dK))
    for i in dK.keys():
        # 현재 체력 이상의 대미지를 받을 경우 기사는 체스판에서 사라짐
        K[i] = dK[i]
        if dK[i][4] <= 0 :
            del(K[i])
            bye.append(i)
    if isDebug:
        print('-----stage fin. res-----')
        print('K',K)
        print('bye', bye)





for q in Qs:
    i, d = q
    if isDebug: print('***Q***', i, d)
    moveK(i, d) 
    if isDebug: print('dam', dam)

# Q 번의 명령 이후, "생존한 기사들이 총 받은 대미지"의 합 출력
R = 0
for i in range(1, N+1):
    if(isDebug): print('i', i, R)
    if i in K and len(K[i]) > 0:
        if(isDebug): print('dam[i], K[i][4]',R,  i, dam[i], K[i][4], dam[i]-K[i][4])
        R += (dam[i] - K[i][4])

print(R)