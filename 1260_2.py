from collections import deque

N, M, V = map(int, input().split())
d = dict()
for _ in range(M):
    s, e = map(int, input().split())
    if s in d:
        d[s].append(e)
    else:
        d[s] = [e]
    if e in d:
        d[e].append(s)
    else:
        d[e] = [s]

def DFS(s):
    v = []
    q = deque()
    q.append(s)
    while q:
        tmp = q.pop()
        if tmp not in v :
            v.append(tmp)
            if len(v) == N: break
        if tmp in d:
            for dt in d[tmp]:
                if dt not in v:
                    q.append(dt)
    return v

def BFS(s):
    v = []
    q = deque()
    q.append(s)
    while q:
        tmp = q.popleft()
        if tmp not in v :
            v.append(tmp)
            if len(v) == N: break
        if tmp in d:
            for dt in d[tmp]:
                if dt not in v:
                    q.append(dt)
    return v

for de in d:
    d[de].sort(reverse=True)

print(*DFS(V))

for de in d:
    d[de].sort()

print(*BFS(V))