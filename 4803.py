import sys
from collections import deque
input = sys.stdin.readline

def findCycle(s):
    q = deque()
    q.append(s)
    isCycle = False
    while q:
        tmp = q.popleft()
        if v[tmp] :
            isCycle = True
        
        v[tmp] = 1
        for n in g[tmp]:
            if v[n] == 0:
                q.append(n)
    return isCycle

t = 0
while True:
    t += 1
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    v = [0 for _ in range(N+1)]
    g = [[] for _ in range(N+1)]

    for _ in range(M):
        s, e = map(int, input().split())
        g[s].append(e)
        g[e].append(s)
    
    res = 0
    
    for node in range(1, N+1):
        if v[node] == 0:
            if not findCycle(node):
                res += 1
    
    print(f"Case {t}: ", end='')
    if res == 0 :
        print("No trees.")
    elif res == 1:
        print("There is one tree.")
    else:
        print(f"A forest of {res} trees.")
    