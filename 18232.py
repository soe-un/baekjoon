import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 1]

N, M = map(int, input().split())
S, E = map(int, input().split())
t = dict()
for _ in range(M):
    x, y = map(int, input().split())
    if x in t : t[x].append(y)
    else : t[x] = [y]
    if y in t : t[y].append(x)
    else : t[y] = [x]

for i in range(1, N+1):
    for j in range(2):
        di = i + dx[j]
        if 0 < di <= N:
            if i in t : t[i].append(di)
            else: t[i] = [di]

distance = [INF for _ in range(N+1)]

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        if now in t :
            for i in t[now]:
                cost = dist + 1
                if cost < distance[i]:
                    distance[i] = cost
                    heapq.heappush(q, (cost, i))

dijkstra(S)


print(distance[E])