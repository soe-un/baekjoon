# 주사위 굴리는 로직
# 주사위의 top, bottom, west, east, north, south 정보를 기억하고 있어야 함

# 동쪽으로 움직이면
# 기존 -> 지금
# west가 top이 됨
# east가 bottom이 됨
# top이 east가 됨
# bottom이 west가 됨
# north, south 그대로

# 서쪽으로 움직이면
# 기존 -> 지금
# west가 bottom이 됨
# east가 top이 됨
# top이 west가 됨
# bottom이 east가 됨
# north, south 그대로

# 북쪽으로 움직이면
# 기존 -> 지금
# west, east 그대로
# top이 north가 됨
# bottom이 south가 됨
# north가 bottom이 됨
# south가 top이 됨

# 남쪽으로 움직이면
# 기존 -> 지금
# west, east 그대로
# top이 south가 됨
# bottom이 north가 됨
# north가 top이 됨
# south가 bottom이 됨

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

dice = {
    'top': 0,
    'bottom': 0,
    'west': 0,
    'east': 0,
    'north': 0,
    'south': 0
}

def moveDice(direction):
    if direction == 1: #동쪽
        dice['top'], dice['bottom'], dice['east'], dice['west'] = dice[
            'west'], dice['east'], dice['top'], dice['bottom']
    elif direction == 2: #서쪽
        dice['bottom'], dice['top'], dice['west'], dice['east'] = dice[
            'west'], dice['east'], dice['top'], dice['bottom']
    elif direction == 3: #북쪽
        dice['north'], dice['south'], dice['bottom'], dice['top'] = dice[
            'top'], dice['bottom'], dice['north'], dice['south']
    elif direction == 4: #남쪽
        dice['south'], dice['north'], dice['top'], dice['bottom'] = dice[
            'top'], dice['bottom'], dice['north'], dice['south']



N, M, Y, X, K = map(int, input().split())
g = []
for _ in range(N):
    g.append(list(map(int, input().split())))
c = list(map(int, input().split()))

for t in range(K):
    dir = c[t]
    # 주사위가 지도 내부에 있을 수 있는지 체크
    ix = X + dx[dir-1]
    iy = Y + dy[dir-1]
    if not(0 <= ix < M and 0 <= iy < N): 
        continue

    # 주사위 굴리고
    moveDice(dir)
    # x,y 좌표 바꾸고
    X = ix
    Y = iy

    if(g[Y][X] == 0):
        g[Y][X] = dice['bottom']
    else:
        dice['bottom'] = g[Y][X]
        g[Y][X] = 0
    print(dice['top'])

