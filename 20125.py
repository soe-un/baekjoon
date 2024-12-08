import sys

N = int(sys.stdin.readline())

cookie = []
for i in range(N):
    tmp = sys.stdin.readline().strip()
    cookie.append(tmp)

# 심장 찾기
# 머리를 찾은 다음, (위부터 찾아서 맨 처음 *이 있는 위치)
# 그 바로 아래가 심장
heart = (0, 0)
for i in range(N):
    if '*' in cookie[i]:
        heart = (i+1, cookie[i].index('*'))
        break

# 팔 길이 구하기
# 왼쪽
leftArm = heart[1]
for j in range(0, heart[1]):
    if(cookie[heart[0]][j] == '*'):
        leftArm = heart[1] - j
        break

# 오른쪽
rightArm = N - heart[1] - 1
for j in range(heart[1]+1, N):
    if(cookie[heart[0]][j] == '_'):
        rightArm = j - heart[1] - 1
        break

# 허리 길이 구하기
body = 0
startedBottom = 0
for j in range(heart[0]+1, N):
    if('*_*' in cookie[j]): # 다리 시작 패턴
        body = j - heart[0] - 1
        startedBottom = j
        break

# 다리 길이 구하기
# 왼쪽
leftLeg = N - startedBottom
for j in range(startedBottom, N):
    if(cookie[j][heart[1]-1] == '_'):
        leftLeg = j - startedBottom
        break

# 오른쪽
rightLeg = N - startedBottom
for j in range(startedBottom, N):
    if(cookie[j][heart[1]+1] == '_'):
        rightLeg = j - startedBottom
        break


print(heart[0]+1, heart[1]+1)
print(leftArm, rightArm, body, leftLeg, rightLeg)
