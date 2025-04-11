# 1. 시간의 벽에서 탈출하기
# 필요한 것: 출구 위치
# def outofTimeWall (er, ec):

N, M, F = map(int, input().split())
space = []
timeV = []
startMIdx = None
exitPosition = None
for i in range(N):
    inputS = list(map(int, input().split()))
    space.append(inputS)
    if startMIdx == None and 3 in inputS:
        startMIdx = (i, inputS.index(3))
# 동 - 0 서 - 1 남 - 2 북 - 3 위 - 4
time3D = []
for _ in range(5):
    time2D = []
    for _ in range(M):
        time2D.append(list(map(int, input().split())))
    time3D.append(time2D)

for _ in range(F):
    timeV.append(list(map(int, input().split())))

print('space')
for s in space:
    print(s)

# 0. 출구 위치 구하기
# 3 range
mr, mc = startMIdx
print(range(max(0, mr-1), min(N-1, mr+M+1)))
print(range(max(0, mc-1), min(N-1, mc+M+1)))
for r in range(max(0, mr-1), min(N-1, mr+M+1)):
    for c in range(max(0, mc-1), min(N-1, mc+M+1)):
        if space[r][c] == 0:
            exitPosition = (r, c)
            break
print(exitPosition)
