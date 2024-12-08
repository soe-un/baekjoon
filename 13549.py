# 수빈이는 동생과 숨바꼭질을 하고 있다.
# 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고,
# 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
# 수빈이는 걷거나 순간이동을 할 수 있다.
# 만약, 수빈이의 위치가 X일 때
# 걷는다면
# 1초 후에 X-1 또는 X+1로 이동하게 된다.
# 순간이동을 하는 경우에는
# 0초 후에 2*X의 위치로 이동하게 된다.

# 수빈이와 동생의 위치가 주어졌을 때,
# 수빈이가 동생을 찾을 수 있는
# 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

limit = 100001
time = [0] * limit

def bfs(x, y):
    q = deque()
    if x == 0:
        q.append(1)
    else:
        q.append(x)
    
    while q:
        x = q.popleft()
        if y == x :
            return time[x]
        for nx in (x-1, x+1, x*2):
            if 0 <= nx < limit and time[nx] == 0:
                if nx == 2*x:
                    time[nx] = time[x]
                    q.appendleft(nx)
                else :
                    time[nx] = time[x] +1
                    q.append(nx)


if(N == 0):
    if(K == 0):
        print(0)
    else:
        print(bfs(N, K) + 1)
else:
    print(bfs(N, K))