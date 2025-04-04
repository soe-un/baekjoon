from collections import deque
def dfs(s, g):
    global N
    v = []
    t = deque()
    t.append(s)

    while t:
        c = t.pop()
        if c not in v: 
            v.append(c)
            if(len(v) == N): break
        if c in g:
            g[c].sort(reverse=True)
            for gc in g[c]:
                if gc not in v:
                    t.append(gc)
    return v


def bfs(s, g):
    global N
    v = []
    t = deque()
    t.append(s)

    while t:
        c = t.pop(0)
        if c not in v: 
            v.append(c)
            if(len(v) == N): break
        if c in g:
            g[c].sort()
            for gc in g[c]:
                if gc not in v:
                    t.append(gc)
    return v

N, M, V = map(int, input().split())
graph = dict()

for _ in range(M):
    s, e = map(int, input().split())
    if s in graph:
        graph[s].append(e)
    else:
        graph[s] = [e]
    if e in graph:
        graph[e].append(s)
    else:
        graph[e] = [s]

d = dfs(V, graph)
b = bfs(V, graph)

print(*d)
print(*b)
