N, M = map(int, input().split())
town = []
home = []
for _ in range(N):
    town.append(list(map(int, input().split())))

home = []
chicken = []

for r in range(N):
    for c in range(N):
        if town[r][c] == 1:
            home.append((r, c))
        if town[r][c] == 2:
            chicken.append((r, c))

cN = len(chicken)

def getDis(h, c):
    hr, hc = h
    cr, cc = c
    return abs(hr - cr) + abs(hc - cc)

def findChickenDis(chickens):
    cityChickenDist = 0

    for h in home:
        homeChickenDist = 100
        for c in chickens:
            td = getDis(h, c)
            if td <= homeChickenDist:
                homeChickenDist = td
        cityChickenDist += homeChickenDist
    return cityChickenDist


def combinations(array, r):
    for i in range(len(array)):
        if r == 1: # 종료 조건
            yield [array[i]]
        else:
            for next in combinations(array[i+1:], r-1):
                yield [array[i]] + next

surviveChickenCase = list(combinations(chicken, M))
res = 1000000
for sc in surviveChickenCase:
    tmp = findChickenDis(sc)
    if res > tmp : res = tmp

print(res)
