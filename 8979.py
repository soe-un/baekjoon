import sys

N, K = map(int, sys.stdin.readline().split())
record = dict()

for _ in range(N):
    n, g, s, b = map(int, sys.stdin.readline().split())
    record[n] = [g, s, b]

def findGoodNation() :
    global record
    res = 0
    # 나보다 더 잘한 나라 수 구하기

    # 1. 금메달이 더 많은 국가 찾기
    f = list(filter(lambda x:record[x][0] > record[K][0], record))
    fLen = len(f)
    if(fLen == 0):
        return 0
    else:
        res += fLen
        # 2-1. 금메달이 같은 국가가 있는지 찾기 // 없으면 리턴
        s1 = list(filter(lambda x:record[x][0] == record[K][0], f))
        if(len(s1) == 0):
            return res
        else: # // 있으면 은메달이 더 많은 국가 찾기
            s2 = list(filter(lambda x:record[x][1] > record[K][1], s1))
            s2Len = len(s2)
            if(s2Len == 0):
                return res
            else :
                res += s2Len
                # 3. 금메달과 은메달이 같은 국가가 있는지 찾기 // 없으면 리턴
                b1 = list(filter(lambda x:record[x][1] == record[K][1], s2))
                if(len(b1) == 0):
                    return res
                else : # // 있으면 동메달이 더 많은 국가 찾기
                    b2 = list(filter(lambda x:record[x][2] > record[K][2], b1))
                    return res + len(b2)

    
print(findGoodNation()+1)