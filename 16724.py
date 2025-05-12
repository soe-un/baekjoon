import sys

input = sys.stdin.readline
N, M = map(int, input().split())
g = []
for _ in range(N):
    g.append(list(input().strip()))

v = [[False for _ in range(M)] for _ in range(N)] 

res = 0

def findCycle(r, c):
    global res
    v[r][c] = True
    cycle.append((r, c))

    if g[r][c] == 'U' and r > 0:
        r -= 1
    elif g[r][c] == 'D' and r < N - 1:
        r += 1
    elif g[r][c] == 'L' and c > 0:
        c -= 1
    elif g[r][c] == 'R' and c < M - 1:
        c += 1
    
    if v[r][c]:
        if (r, c) in cycle:
            res += 1
    else:
        findCycle(r, c)

for i in range(N):
    for j in range(M):
        if not v[i][j]:
            cycle = []
            findCycle(i, j)

            
print(res)