import sys
N = int(sys.stdin.readline())

numbox = 1
cnt = 1

while N > numbox:
    numbox += 6 * cnt
    cnt += 1
    
print(cnt)
