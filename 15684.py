isDebug = False
# 한 라인에 2 * n개의 가로선을 만들어야 함.
N, M, H = map(int, input().split())
V = dict()
for m in range(M):
    a, b = list(map(int, input().split()))
    if b in V:
        V[b].append(a)
    else:
        V[b] = [a]
if isDebug: print('V', V)
def getRes():
    global N, H, V
    glv = range(len(V))
    vKeys = list(V.keys())
    vKeys.sort()
    if isDebug: print('vKeys', vKeys)
    res = 0
    haveToAddLineH = dict()
    # b가 같은 모든 가로선의 개수를 체크하고,
    for i in glv:
        v = V[vKeys[i]]
        if isDebug: print('v', v)
        lv= len(v)
        # 짝수라면 넘어가기
        if lv % 2 == 0:
            continue
        else :
            # 홀수라면 가로선의 개수가 H와 동일한지 체크하고
            if lv <= H:
                # 아니라면 추가하는 라인이 이전 또는 다음 세로선과 겹치는지 확인하고
                canH = set(range(1, H+1))  - set(v)
                if isDebug: print('canH', canH, set(range(1, H+1)), set(v))

                if i+1 < lv:
                    nextH = set(V[vKeys[i+1]])
                    if isDebug: print('nextH', nextH)
                    canH = canH - nextH
                if i-1 >= 0:
                    prevH = set(V[vKeys[i-1]])
                    if isDebug: print('prevH', prevH)
                    canH = canH - prevH
                
                if isDebug: print('rescanH', canH)
                # 라인을 추가해야 하는데 현 상태에서는 추가할 방도가 없음
                if len(canH) <= 0:
                    return -1
                # 추가할 수 있는 위치를 추가해야 하는 리스트에 저장
                haveToAddLineH[i+1] = canH
            else:
                return -1
    if isDebug: print(haveToAddLineH)
    lHAL = len(haveToAddLineH)
    # 추가해야 하는 라인이 3개 이상이면 -1
    if lHAL > 3 : return -1 
    # 추가할 수 있는 위치인지 파악
    # 필요한 라인이 얼마나 이어져 있는가?
    lineCheck = list(haveToAddLineH.keys())
    lineCheck.sort()
    if isDebug: print('lineCheck', lineCheck)
    cPosition = []
    for i in range(len(lineCheck)-1):
        if lineCheck[i] == lineCheck[i+1] -1 :
            cPosition = [lineCheck[i], lineCheck[i+1]]
        if i == 1 and lineCheck[i-1] + 1 == lineCheck[i] == lineCheck[i+1] - 1:
            cPosition = [lineCheck[i-1], lineCheck[i], lineCheck[i+1]]
            break

    if isDebug: print('cPosition', cPosition)

    cL = len(cPosition)
    # 1. 3 라인이 이어져 있음
    if cL == 3:
        # 겹치는 수 확인
        fH = set(haveToAddLineH[cPosition[0]])
        sH = set(haveToAddLineH[cPosition[1]])
        tH = set(haveToAddLineH[cPosition[2]])
        lfH = len(fH)
        lsH = len(sH)
        ltH = len(tH)
        fsI = fH.intersection(sH)
        stI = sH.intersection(tH)
        allI = fsI.intersection(tH)
        if isDebug: print('intersection', fsI, stI, allI)
        if len(fsI) == 0 and len(stI) == 0 :
            return lHAL
        # 겹치는 수가 3개라면 가장 작은 경우의 수를 제외한 나머지 2개가
        # 겹치는 곳 이외에 다른 곳이 둘 다 있는지 확인, 없으면 False
        if len(allI) >= 1:
            if lfH >= 2 and lsH >= 2 and ltH >= 2:
                if fH == sH == tH: return -1
                return lHAL
            elif lfH == 1 and lsH >= 2 and ltH >= 2:
                if len(sH - allI) > 0 and len(tH - allI):
                    return lHAL
                else: return -1
            elif lfH >= 2 and lsH == 2 and ltH >= 2:
                if len(fH - allI) > 0 and len(tH - allI):
                    return lHAL
                else: return -1
            elif lfH >= 2 and lsH >= 2 and ltH == 2:
                if len(fH - allI) > 0 and len(sH - allI):
                    return lHAL
                else: return -1
        # 겹치는 수가 2개라면 서로 겹치는 두 곳을 뺐을 때
        # 하나 이상의 경로가 남지 않으면 False
        elif fsI >= 1:
            mFS = fH - sH
            mSH = sH - fH
            if len(mFS) > 0 or len(mSH) > 0 : return lHAL
            else: return -1
        elif stI >= 1:
            mST = sH - tH
            mTS = tH - sH
            if len(mST) > 0 or len(mTS) > 0 : return lHAL
            else: return -1
    # 2. 2 라인만 이어져 있음 -> 한 라인은 그냥 추가하고,
    # 2 라인에 대해 서로 겹치지 않는다면 그냥 추가.
    # 겹친다면 개수가 2개 이상인지 파악하고 겹치는데 1개라면 false
    elif cL == 2:
        if lHAL == 3 : res += 1
        fH = set(haveToAddLineH[cPosition[0]])
        sH = set(haveToAddLineH[cPosition[1]])
        if len(fH.intersection(sH)) == 1 and len(fH) == 1 and len(sH) == 1 :
            return -1
        else: res += 2

        return
    # 3. 모두 따로따로 있음 -> 그냥 추가하면 됨. length만큼 res에 추가
    elif cL == 0:
        res += lHAL


    if res > 3 : return -1
    else : return res

print(getRes())