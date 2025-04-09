isDebug = True
R, C, K = map(int, input().split())
R -= 1
C -= 1
arr = []
for _ in range(3):
    arr.append(list(map(int, input().split())))
calLen = 3

def RCal() :
    
    for i in range(calLen):
        J = arr[i]
        ad = dict()
        for j in J:
            if j in ad : ad[j] += 1
            else: ad[j] = 1
        if isDebug: print('ad', ad)
        print(list(ad))

RCal()