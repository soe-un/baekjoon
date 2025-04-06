from collections import deque
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

N, M = map(int, input().split())
board = []
R = (0, 0)
B = (0, 0)
for n in range(N):
    line = list(input())
    if 'R' in line:
        iR = line.index('R')
        R = (iR, n)
        line[iR] = '.'
    if 'B' in line:
        iB = line.index('B')
        B = (iB, n)
        line[iB] = '.'
    board.append(line)

def bfs() :
    v = []
    t = deque()
    t.append((R, B))
    turn = 0
    while t:
        turn += 1
        if(turn > 10): return -1
        tR, tB = t.popleft()
        v.append((tR, tB))
        



print(bfs())