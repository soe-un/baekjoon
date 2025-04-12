N = int(input())
res = 0
a, b, c = [False]*N, [False]*(2*N-1), [False]*(2*N-1)

def tracking(cnt):
    global res
    if cnt == N:
        res += 1
        return
    
    for j in range(N):
        if not (a[j] or b[cnt+j] or c[cnt-j+N-1]):
            a[j] = b[cnt+j] = c[cnt-j+N-1]=True
            tracking(cnt+1)
            a[j] = b[cnt+j] = c[cnt-j+N-1]=False

tracking(0)
print(res)
