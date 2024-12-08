import sys

N = int(sys.stdin.readline())
people = dict()

for i in range(N):
    x, y = map(int, (sys.stdin.readline().split()))
    people[i] = (x, y)


res = []
for p in people:
    # if()
    res.append(len(list(filter(lambda x:people[x][0] > people[p][0] and people[x][1] > people[p][1], people))) + 1)

for r in res:
    print(r, end=" ")