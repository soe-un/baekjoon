isDebug = False
g = []
for _ in range(4):
    g.append(list(map(int, input())))
K = int(input())
C = []
for _ in range(K):
    C.append(list(map(int, input().split())))

def turnTime(l):
    l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7] = l[
        7], l[0], l[1], l[2], l[3], l[4], l[5], l[6]

def turnReverseTime(l):
    l[0], l[1], l[2], l[3], l[4], l[5], l[6], l[7] = l[
        1], l[2], l[3], l[4], l[5], l[6], l[7], l[0]

for c in C:
    gn, td = c
    gn -= 1

    haveToChangeFirstConnects = []
    haveToChangeSecondConnects = []
    haveToChangeThirdConnects = []
    if gn - 1 >= 0 :
        if g[gn-1][2] != g[gn][6] :
            haveToChangeFirstConnects.append(gn-1)
    if gn + 1 < 4 :
        if g[gn][2] != g[gn+1][6] :
            haveToChangeFirstConnects.append(gn+1)
    if isDebug: print('haveToChangeFirstConnects', haveToChangeFirstConnects)
    for hF in haveToChangeFirstConnects:
        if hF - 1 >= 0 and hF-1 != gn:
            if g[hF-1][2] != g[hF][6] :
                if hF-1 not in haveToChangeFirstConnects:
                    haveToChangeSecondConnects.append(hF-1)
        if hF + 1 < 4 and hF+1 != gn:
            if g[hF][2] != g[hF+1][6] :
                if hF+1 not in haveToChangeFirstConnects:
                    haveToChangeSecondConnects.append(hF+1)
    if isDebug: print('haveToChangeSecondConnects', haveToChangeSecondConnects)
    for hS in haveToChangeSecondConnects:
        if hS - 1 >= 0 and hS-1 != gn:
            if g[hS-1][2] != g[hS][6] :
                if hS-1 not in haveToChangeFirstConnects and hS-1 not in haveToChangeSecondConnects :
                    haveToChangeThirdConnects.append(hS-1)
        if hS + 1 < 4 and hS+1 != gn:
            if g[hS][2] != g[hS+1][6] :
                if hS+1 not in haveToChangeFirstConnects and hS+1 not in haveToChangeSecondConnects :
                    haveToChangeThirdConnects.append(hS+1)
    if isDebug: print('haveToChangeSecondConnects', haveToChangeThirdConnects)
    # 첫번째 회전
    if td == 1: # 시계방향일 경우
        turnTime(g[gn])
        for hF in haveToChangeFirstConnects:
            turnReverseTime(g[hF])
        for hS in haveToChangeSecondConnects:
            turnTime(g[hS])
        for hT in haveToChangeThirdConnects:
            turnReverseTime(g[hT])
    elif td == -1 : # 반시계방향인 경우
        turnReverseTime(g[gn])
        for hF in haveToChangeFirstConnects:
            turnTime(g[hF])
        for hS in haveToChangeSecondConnects:
            turnReverseTime(g[hS])
        for hT in haveToChangeThirdConnects:
            turnTime(g[hT])
    
        
res = 0
if g[0][0] == 1 : res += 1
if g[1][0] == 1 : res += 2
if g[2][0] == 1 : res += 4
if g[3][0] == 1 : res += 8

print(res)