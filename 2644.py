from collections import deque

N = int(input())
S, E = map(int, input().split())
M = int(input())
relation = dict()
chonsu = [0 for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    if i in relation:
        relation[i].append(j)
    else: 
        relation[i] = [j]
    if j in relation:
        relation[j].append(i)
    else:
        relation[j] = [i]


def dfs(s, e):
    global chonsu
    v = []
    t = deque()

    t.append(s)

    while t:
        tmp = t.pop()
        if(tmp not in v):
            v.append(tmp)
            if tmp == e:
                return v
            if tmp in relation:
                for tc in relation[tmp]:
                    if tc not in v:
                        t.append(tc)
                        chonsu[tc] += chonsu[tmp]+ 1
    return -1

dfs(S, E)
if chonsu[E] == 0 : print(-1)
else: print(chonsu[E])
