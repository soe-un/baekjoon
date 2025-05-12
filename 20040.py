import sys
input = sys.stdin.readline

N, M = map(int, input().split())
p = [i for i in range(N)]

def find(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    px = find(x)
    py = find(y)
    if px < py:
        p[py] = px
    else :
        p[px] = py

res = 0
for i in range(M):
    x, y = map(int, input().split())
    if find(x) == find(y):
        res = i + 1
        break
    union(x, y)

print(res)