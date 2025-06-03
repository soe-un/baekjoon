from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
S, E = map(int, input().split())
M = int(input())
family = dict()

for _ in range(M):
    x, y = map(int, input().split())
    if x in family : family[x].append(y)
    else : family[x] = [y]

    if y in family : family[y].append(x)
    else : family[y] = [x]


def dfs(s, e):
    v = []
    q = deque()
    q.append([s, 0])

    while q:
        n, val = q.pop()
        if n == e:
            return val
        
        if n in family:
            for x in family[n]:
                if x not in v:
                    q.append([x, val+1])
                    v.append(x)
    return -1

print(dfs(S, E))