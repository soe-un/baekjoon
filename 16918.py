import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

R, C, N = map(int, input().split())
m = []
for _ in range(R):
    m.append(list(input().strip()))


if N == 1:
    for mm in m:
        print(''.join(mm))
else:
    for i in range(R):
        for j in range(C):
            if m[i][j] == 'O':
                m[i][j] = 2
            else :
                m[i][j] = 0


    def turnRes(n):
        global m, R, C
        for i in range(2,n+1):
            if i % 2 == 0:
                for r in range(R):
                    for c in range(C):
                        if m[r][c] == 0: m[r][c] = 3
                        else: m[r][c] -= 1
            else: 
                bombList = []
                for r in range(R):
                    for c in range(C):
                        if m[r][c] == 1: bombList.append((r, c))
                        else: m[r][c] -= 1
                for b in bombList:
                    x, y = b
                    m[x][y] = 0
                    for k in range(4):
                        ix, iy = x + dx[k], y + dy[k]
                        if 0 <= ix < R and 0 <= iy < C :
                            m[ix][iy] = 0

    if N % 2 == 0:
        for i in range(R):
            print(''.join(['O' for _ in range(C)]))
    else:
        if N > 2 and N % 4 == 1: turnRes(5)
        elif N > 2 and N % 4 == 3: turnRes(3)
        for r in range(R):
            for c in range(C):
                if m[r][c] == 0 : print('.', end='')
                else: print('O', end='')
            print()