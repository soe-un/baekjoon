N, M = map(int, input().split())
p = []
for _ in range(N):
    p.append(list(map(int, input().split())))

# 가로 기원 항목 찾기
def findXTetromino (s):
    x, y = s
    if x + 1 >= M :
        return 0
    
    base = p[y][x] + p[y][x+1]
    xSums = []
    # 앞으로 나아가면서 진행할 것이기 때문에, x의 이전 항목은 체크할 필요 없음
    # 1번 형태
    # 위
    if y - 1 >= 0:
        xSums.append(base + p[y-1][x] + p[y-1][x+1])
    # 아래
    if y + 1 < N:
        xSums.append(base + p[y+1][x] + p[y+1][x+1])
    
    # 2번 형태
    # 오른쪽
    if x + 3 < M :
        xSums.append(base + p[y][x+2] + p[y][x+3])

    # 3번 형태
    # 위
    if y - 2 >= 0 :
        xSums.append(base + p[y-1][x] + p[y-2][x])
        xSums.append(base + p[y-1][x+1] + p[y-2][x+1])
    # 아래
    if y + 2 < N :
        xSums.append(base + p[y+1][x] + p[y+2][x])
        xSums.append(base + p[y+1][x+1] + p[y+2][x+1])
    
    if y - 1 >= 0 and y + 1 < N:
        # 4번 형태
        # 왼쪽-위
        xSums.append(base + p[y-1][x] + p[y+1][x+1])
        # 오른쪽-위
        xSums.append(base + p[y-1][x+1] + p[y+1][x])
    
        # 5번 형태
        # 왼쪽
        xSums.append(base + p[y-1][x] + p[y+1][x])
        # 오른쪽
        xSums.append(base + p[y-1][x+1] + p[y+1][x+1])
    return max(xSums)

# 세로 기원 항목 찾기
def findYTetromino (s):
    x, y = s
    if y + 1 >= N :
        return 0
    base = p[y][x] + p[y+1][x]
    ySums = []
    # 아래로 나아가면서 진행할 것이기 때문에, y의 이전 항목은 체크할 필요 없음
    # 1번 형태
    # 뒤
    if x - 1 >= 0 :
        ySums.append(base + p[y][x-1] + p[y+1][x-1])
    # 앞
    if x + 1 < M:
        ySums.append(base + p[y][x+1] + p[y+1][x+1])
    
    # 2번 형태
    # 아래
    if y + 3 < N :
        ySums.append(base + p[y+2][x] + p[y+3][x])
    
    # 3번 형태
    # 왼쪽
    if x - 2 >= 0:
        ySums.append(base + p[y][x-1] + p[y][x-2])
        ySums.append(base + p[y+1][x-1] + p[y+1][x-2])
    if x + 2 < M :
        ySums.append(base + p[y][x+1] + p[y][x+2])
        ySums.append(base + p[y+1][x+1] + p[y+1][x+2])
    
    if x - 1 >= 0 and x + 1 < M :
        # 4번 형태
        ySums.append(base + p[y][x-1] + p[y+1][x+1])
        ySums.append(base + p[y+1][x-1] + p[y][x+1])

        # 5번 형태
        ySums.append(base + p[y][x-1] + p[y][x+1])
        ySums.append(base + p[y+1][x-1] + p[y+1][x+1])

    return max(ySums)

maxRes = 0

for i in range(N):
    for j in range(M):
        mX = findXTetromino((j, i))
        mY = findYTetromino((j, i))
        if maxRes <= mX : maxRes = mX
        if maxRes <= mY : maxRes = mY

print(maxRes)