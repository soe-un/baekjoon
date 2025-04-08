from collections import deque
isDebug = False

N, M, K = map(int, input().split())
A = []
tree = deque()
for _ in range(N):
    A.append(list(map(int, input().split())))

for _ in range(M):
    tree.append(list(map(int, input().split())))

# 기본 땅
ground= [[5 for i in range(N)] for j in range(N)]
deathTree = deque()


def spring():
    global deathTree, ground, tree
    tl = len(tree)
    
    for i in range(tl):
        x, y, age = tree[i]

        # 만약 땅에 양분이 나이만큼 있다면
        # 나무가 나이만큼 양분을 먹고
        # 나이가 1 증가함
        if(ground[x-1][y-1] >= age):
            ground[x-1][y-1] -= age
            tree[i][2] += 1
        # 땅에 양분이 나이만큼 없다면
        # 즉시 나무는 죽는다
        else:
            deathTree.append(tree[i])
    for d in deathTree:
        tree.remove(d)
    if isDebug:
        print('*****SPRING end...*****')
        print('ground')
        for g in ground:
            print(g)
        print('tree, deathTree', tree,deathTree)


def summer():
    global deathTree, ground
    for dt in deathTree:
        # 죽은 나무가 양분으로 변한다
        # 죽은 나무의 나이 // 2 가 칸에 추가
        x, y, age = dt
        ground[x-1][y-1] += (age // 2) 
    deathTree = []
    
    if isDebug:
        print("*****SUMMER end ...*****")
        print('ground')
        for g in ground:
            print(g)
        print('deathTree',deathTree)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def fall():
    global tree
    tl = len(tree)
    # 나이가 5의 배수인 나무의
    # 인접한 8칸(N x N 안)에 나이가 1인 나무가 생긴다
    for i in range(tl):
        x, y, age = tree[i]
        idxX, idxY = x-1, y-1
        if age % 5 == 0:
            for i in range(8):
                if 0 <= idxX+dx[i] < N and 0 <= idxY+dy[i] <N:
                    tree.append([idxX+dx[i] + 1, idxY+dy[i]+1, 1])
    if isDebug:
        print("*****FALL end ...*****")
        print('tree', tree)

def winter():
    global ground
    # S2D2가 땅에 양분을 추가한다.
    for j in range(N):
        for i in range(N):
            ground[j][i] += A[j][i]
    if isDebug:
        print("*****winter end ...*****")
        print('ground')
        for g in ground:
            print(g)

for k in range(K):
    spring()
    summer()
    fall()
    winter()

print(len(tree))