from collections import deque

C = int(input())
P = int(input())
network = dict()
for _ in range(P):
    s, e = map(int, input().split())
    if s in network: network[s].append(e)
    else: network[s] = [e]
    if e in network: network[e].append(s)
    else: network[e] = [s]

def dfs(s):
    v = []
    t = deque()
    t.append(s)

    while t:
        tmp = t.pop()
        if tmp not in v:
            v.append(tmp)
            if tmp in network:
                for n in network[tmp]:
                    if n not in v:
                        t.append(n)
    return len(v)
print(dfs(1)-1)