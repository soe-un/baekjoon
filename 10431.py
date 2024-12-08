import sys

P = int(sys.stdin.readline())

for _ in range(P): 
    inputCase = list(map(int, sys.stdin.readline().split()))
    cnt = 0
    for i in range(1, len(inputCase)-1): # it will be always 21
        for j in range(i+1, len(inputCase)): # it will be always 20
            if(inputCase[i]> inputCase[j]) :
                inputCase[i], inputCase[j] = inputCase[j], inputCase[i]
                cnt += 1
    
    print(inputCase[0], cnt)