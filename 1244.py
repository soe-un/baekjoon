# 1부터 연속적으로 번호가 붙어있는 스위치들이 있다.
# 스위치는 켜져 있거나 꺼져있는 상태이다.
# <그림 1>에 스위치 8개의 상태가 표시되어 있다.
# ‘1’은 스위치가 켜져 있음을, ‘0’은 꺼져 있음을 나타낸다.
# 그리고 학생 몇 명을 뽑아서, 학생들에게 
# 1 이상이고 스위치 개수 이하인 자연수를 하나씩 나누어주었다. 
# 학생들은 자신의 성별과 받은 수에 따라 
# 아래와 같은 방식으로 스위치를 조작하게 된다.

# 남학생은 스위치 번호가 자기가 받은 수의 배수이면, 
# 그 스위치의 상태를 바꾼다. 
# 즉, 스위치가 켜져 있으면 끄고, 
# 꺼져 있으면 켠다. 
# <그림 1>과 같은 상태에서 
# 남학생이 3을 받았다면, 이 학생은 
# <그림 2>와 같이 
# 3번, 6번 스위치의 상태를 바꾼다.

# 여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 
# 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 
# 그 구간에 속한 스위치의 상태를 모두 바꾼다. 
# 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.

# 예를 들어 <그림 2>에서 여학생이 3을 받았다면, 
# 3번 스위치를 중심으로
# 2번, 4번 스위치의 상태가 같고 
# 1번, 5번 스위치의 상태가 같으므로, 
# <그림 3>과 같이 1번부터 5번까지 스위치의 상태를 모두 바꾼다. 
# 만약 <그림 2>에서 여학생이 4를 받았다면, 
# 3번, 5번 스위치의 상태가 서로 다르므로 
# 4번 스위치의 상태만 바꾼다.

# 입력으로 스위치들의 처음 상태가 주어지고, 
# 각 학생의 성별과 받은 수가 주어진다. 
# 학생들은 입력되는 순서대로 
# 자기의 성별과 받은 수에 따라 
# 스위치의 상태를 바꾸었을 때, 
# 스위치들의 마지막 상태를 출력하는 프로그램을 작성하시오.

import sys

S = int(sys.stdin.readline())
switches = list(map(int, sys.stdin.readline().split()))
studentCnt = int(sys.stdin.readline())
students = []
for c in range(studentCnt):
    students.append(list(map(int, sys.stdin.readline().split())))

for student in students:
    if(student[0] == 1):
        # 남학생 : 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다. 
        num = student[1]
        idx = student[1]-1
        for i in range(idx, S, num):
            switches[i] = abs(switches[i]-1)
    else:
        # 여학생 : 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 
        # 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서, 
        # 그 구간에 속한 스위치의 상태를 모두 바꾼다. 
        # 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.

        # 0이나 S-1일 경우 주변 탐지가 불가능하므로 하나만 바꿔준다.
        num = student[1]
        idx = student[1]-1
        if(num == 1 or num == S):
            switches[idx] = abs(switches[idx] - 1)
            continue

        startPoint = idx
        endPoint = idx
        while True:
            if(switches[startPoint] == switches[endPoint]):
                if(startPoint - 1 < 0 or endPoint + 1 > S-1):
                    break
                startPoint -= 1
                endPoint += 1
            else:
                startPoint += 1
                endPoint -= 1
                break
        for i in range(startPoint, endPoint+1):
            switches[i] = abs(switches[i]-1)


if(S > 20):
    while True:
        if(len(switches) < 20):
            print(*switches)
            break
        print(*switches[:20])
        switches = switches[20:]

else: print(*switches)