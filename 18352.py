import sys
import heapq
INF = 300001
input = sys.stdin.readline
N, M, K, X = map(int, input().split())
g = dict()
dis = [INF for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    if x in g: g[x].append(y)
    else: g[x] = [y]

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    dis[s] = 0
    while q:
        d, n = heapq.heappop(q)
        if dis[n] < d:
            continue
        if n in g:
            for next in g[n]:
                cost = dis[n] + 1
                if cost < dis[next]:
                    dis[next] = cost
                    heapq.heappush(q, (cost, next))

dijkstra(X)
if K not in dis:
    print(-1)
else:
    for i in range(1, N+1):
        if dis[i] == K: print(i)