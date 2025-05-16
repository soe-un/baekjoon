import sys
input = sys.stdin.readline

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

R, C = map(int, input().split())
m = [list(input().strip()) for _ in range(R)]

def getFarm():
    for i in range(R):
        for j in range(C):
            if m[i][j] == 'W':
                for k in range(4):
                    ir, ic = i + dr[k],  j + dc[k]
                    if 0 <= ir < R and 0 <= ic < C :
                        if m[ir][ic] == 'S': return False
            elif m[i][j] == '.':
                m[i][j] = 'D'
    return True

if getFarm() :
    print('1')
    for me in m:
        for i in me:
            print(i, end="")
        print('')
else: print(0)

