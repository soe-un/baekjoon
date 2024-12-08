# 정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 4가지가 있다.
# 합을 나타낼 때는 수를 1개 이상 사용해야 한다.
# 합을 이루고 있는 수의 순서만 다른 것은 같은 것으로 친다.

# 1. 1+1+1+1
# 2. 2+1+1 (1+1+2, 1+2+1)
# 3. 2+2
# 4. 1+3 (3+1)

# 정수 n이 주어졌을 때, 
# n을 1, 2, 3의 합으로 나타내는 방법의 수를
# 구하는 프로그램을 작성하시오.

import sys

T = int(sys.stdin.readline())

def geThreeCase(N):
    cnt = N//3
    res = 0
    for c in range(1, cnt+1):
        tmp = N-(3*c) 
        if (tmp > 1):
            res += (tmp // 2) + 1
        else:
            res += 1
    return res



for _ in range(T):
    n = int(sys.stdin.readline())
    res = 1
    if(n > 1):
        res += (n//2)
    if(n > 2):
        res += geThreeCase(n)
    print(res)
