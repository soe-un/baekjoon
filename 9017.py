# 크로스 컨트리 달리기는 주자들이 
# 자연적인 야외의 지형에 만들어진 코스를 달리는 운동 경기이다. 

# 경주 코스는 일반적으로 4에서 12 킬로미터이며, 
# 숲이나 넓은 땅을 통과하는 풀과 
# 흙으로 된 지면과 언덕과 평평한 지형을 포함한다. 

# 이 경기는 주자들의 개인성적을 매기고, 
# 이를 가지고 팀의 점수를 계산한다. 

# 한 팀은 여섯 명의 선수로 구성되며, 
# 팀 점수는 상위 네 명의 주자의 점수를 합하여 계산한다. 
# 점수는 자격을 갖춘 팀의 주자들에게만 주어지며, 
# 결승점을 통과한 순서대로 점수를 받는다. 
# 이 점수를 더하여 가장 낮은 점수를 얻는 팀이 우승을 하게 된다. 
# 여섯 명의 주자가 참가하지 못한 팀은 점수 계산에서 제외된다. 
# 동점의 경우에는 
# 다섯 번째 주자가 가장 빨리 들어온 팀이 우승하게 된다.

# 예를 들어, 다음의 표를 살펴보자.

# 팀 B 와 D 는 선수의 수가 여섯이 아니므로,
# 점수를 받을 수 없다. 

# 팀 A 의 점수는 18 (1+4+6+7)이고, 
# 팀 C 의 점수는 18 (2+3+5+8)이다. 

# 이 경우 두 팀의 점수가 같으므로 
# 다섯 번째로 결승점을 통과한 선수를 고려한다, 
# A 팀의 다섯 번째 선수의 점수가 
# C 팀의 다섯 번째 선수의 점수보다 적으므로 A 팀이 우승팀이 된다.

# 모든 선수들의 등수가 주어질 때, 
# 우승팀을 구하는 프로그램을 작성하라. 
# 각 팀의 참가 선수가 여섯보다 작으면 
# 그 팀은 점수 계산에서 제외됨을 주의하라. 

# 여섯 명 보다 많은 선수가 참가하는 팀은 없고, 
# 적어도 한 팀은 참가 선수가 여섯이며, 
# 모든 선수는 끝까지 완주를 한다고 가정한다.

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    sData = list(set(data))
    byTeam = dict()
    notTeam = []

    # 6인 이하 제거
    for s in sData:
        if len(list(filter(lambda x:x == s, data))) < 6:
            notTeam.append(s)

    i = 0
    score = 1
    while i < N:
        if data[i] in notTeam:
            i += 1
            continue
        else :
            if (data[i] in byTeam):
                byTeam[data[i]].append(score)
                score += 1
            else:
                byTeam[data[i]] = [score]
                score += 1
            i += 1

    # 1등 계산: 합
    teamSum = [0 for _ in range(len(sData) + 1)] 

    for b in byTeam:
        teamSum[b] = sum(byTeam[b][:4])

    # 단독일 경우 우승
    minScore = min(filter(lambda x:x != 0, teamSum))
    winner = teamSum.index(minScore)

    # 중복일 경우, 5번째가 큰 팀 선택
    winnerList = list(filter(lambda x:x == minScore, teamSum))
    if (len(winnerList) > 1):
        tmp = len(teamSum)
        winnerFifth = byTeam[winner][4]
        for i in range(tmp):
            if(teamSum[i] == minScore and byTeam[i][4] < winnerFifth):
                winnerFifth = byTeam[i][4]
                winner = i
    
    print(winner)

