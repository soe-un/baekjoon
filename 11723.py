import sys
M = int(sys.stdin.readline())
S = set()

for _ in range(M):
    command = sys.stdin.readline().strip().split()
    c = command[0]

    if len(command) == 1:
        if(c == 'all'):
            S = set([i for i in range(1, 21)])
        elif(c == 'empty'):
            S.clear()
    else:
        x = int(command[1])

        if(c == 'add'):
            S.add(x)
        elif(c == 'remove'):
            S.discard(x)
        elif(c == 'check'):
            print(1 if x in S else 0)
        elif(c == 'toggle'):
            if(x in S):
                S.discard(x)
            else:
                S.add(x)
