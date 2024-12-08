from collections import deque
def dfs(graph, startNode):
    visited = list()
    toGoNodes = deque()

    toGoNodes.append(startNode)

    while toGoNodes:
        thisTurnNode = toGoNodes.pop()

        if(thisTurnNode not in visited):
            visited.append(thisTurnNode)
            if(thisTurnNode in graph):
                graph[thisTurnNode].sort(reverse=True)
                toGoNodes += graph[thisTurnNode]
    
    return visited

def bfs(graph, startNode):
    visited = list()
    toGoNodes = list()

    toGoNodes.append(startNode)

    while toGoNodes:
        thisTurnNode = toGoNodes.pop(0)
        if(thisTurnNode not in visited):
            visited.append(thisTurnNode)
            if(thisTurnNode in graph):
                graph[thisTurnNode].sort()
                toGoNodes += graph[thisTurnNode]
    return visited

N, M, V = map(int, input().split())
graph = dict()
for _ in range(M):
    sn, en = map(int, input().split())
    if(sn in graph) : graph[sn].append(en)
    else: graph[sn] = [en]
    if(en in graph) : graph[en].append(sn)
    else: graph[en] = [sn]

dfsRes = dfs(graph, V)
bfsRes = bfs(graph, V)

print(*dfsRes)
print(*bfsRes)
