N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0
for a in A:
    if a - B > 0:
        cnt += 1
        currentA = a-B
        t = (a-B) / C
        tM = (a-B) % C
        # 소수점이 생긴 경우 무조건 올림
        if tM > 0:
            t = int(t) + 1
            cnt += t
        else:
            cnt += int(t)
    else:
        cnt += 1
        continue

print(cnt)