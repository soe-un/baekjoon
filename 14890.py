N, L = map(int, input().split())
m = []
for _ in range(N):
    m.append(list(map(int, input().split())))

debug = False

def findLLengthBlock(l):
    res = []
    s = 0
    e = 0
    while e < N :
        if l[s] == l[e] : 
            if e == N-1 : 
                res.append((s, e))
                break
            e += 1
        else:
            if e - s >= L : 
                res.append((s, e-1))
            s = e
            e = s
    if(debug): print('찾은 쌍! res', res)
    for i in range(len(res)-1, -1, -1) :
        if (res[i][1] - res[i][0]) + 1 < L :
            if(debug): print('경사로 못 놓는 길이라 삭제',res[i][1], res[i][0])
            res.remove(res[i])
    return res

def canGoThisWay(l):
    if l.count(l[0]) == N:
        if(debug): print('ALL SAME!')
        return True
    
    tl = [e for e in l]
    fL = findLLengthBlock(l)

    if len(fL) == 0 :
        if(debug): print('유효한 연속 경사로 놓을 수 없음')
        return False
    
    h = []
    for f in fL:
        fs, fe = f
        if(debug): print('fs, fe', fs, fe)
        canS = False
        canE = False
        # 높이 차이 확인
        if fs - 1 >= 0 :
            if l[fs - 1] == l[fs] + 1:
                if(debug): print('앞에 있음')
                canS = True
        if fe + 1 < N :
            if l[fe + 1] == l[fe] + 1:
                if(debug): print('뒤에 있음')
                canE = True
        if canS and canE: 
            if (fe-fs+1) < 2*L: 
                if(debug): print('둘 다 있는데 너무 짧음',(fe-fs + 1), 2*L)
                return False # 길이가 길지 않으면 둘 중 하나만 성립해야 함
        # start 설치
        if canS:
            # 설치 여부 확인
            for r in range(fs, fs+L):
                if r in h :
                    if(debug): print('이미 설치됨: h, r', h, r)
                    return False
            # 설치
            for r in range(fs, fs+L):
                h.append(r)
                if(debug): print('경사로 설치!: tl, h', tl, h)
        
        # end 설치
        if canE:
            # 설치 여부 확인
            for r in range(fe+1-L, fe+1):
                if r in h :
                    if(debug): print('이미 설치됨: h, r', h, r)
                    return False
            # 설치
            for r in range(fe+1-L, fe+1):
                h.append(r)
                if(debug): print('경사로 설치!: tl, h', tl, h)
    if(debug): print('최종 tl, h', tl, h)
    # 경사로 사용할 수 있으면 통과라네
    val = False
    for vt in range(N-1) :
        if tl[vt] == tl[vt+1]:
            if vt == N-2 :
                val = True
            continue
        # 뒤가 작을 때
        elif tl[vt] - tl[vt+1] == 1:
            if vt+1 in h :
                if vt == N-2 :
                    val = True
                continue
            else:
                if(debug): print('뒤작, 1 차이 나는데 경사로 없음! vt', vt)
                return False
        # 내가 작을 때
        elif tl[vt] - tl[vt+1] == -1:
            if vt in h :
                if vt == N-2:
                    val = True
                continue
            else:
                if(debug): print('내작, 1 차이 나는데 경사로 없음! vt', vt)
                return False
        else:
            if(debug): print('1 이상 차이남, vt', vt)
            return False
        
    
    return val

res = 0
# 가로
for i in range(N):
    thisTurnWay = m[i]
    if(debug): print('가로 i', i)
    if(canGoThisWay(thisTurnWay)):
        res += 1
        if(debug): print("추가요~ res", res)

# 세로
for i in range(N):
    thisTurnWay = []
    for j in range(N):
        thisTurnWay.append(m[j][i])
    if(debug): print('세로 i', i)
    if(canGoThisWay(thisTurnWay)): 
        res += 1
        if(debug): print("추가요~ res", res)

print(res)


