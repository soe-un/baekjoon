import sys
input = sys.stdin.readline

N = int(input())
cards = [*map(int, input().split())]
M = int(input())
scards = [*map(int, input().split())]

res = dict()
for c in cards:
    if c in res:
        res[c] += 1
    else:
        res[c] = 1

for t in scards:
    if t in res:
        print(res[t] , end=" ")
    else:
        print(0, end = " ")