import sys

vowel = ['a','e', 'i', 'o', 'u']

def checkCondition():
    global vowel, password
    # 1. 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
    if len(list(set(password) & set(vowel))) > 0:        
        # 2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
        for i in range(0, len(password) - 2):
            # 모음일 경우
            if((password[i] in vowel) and (password[i+1] in vowel) and (password[i+2] in vowel)):
                return 'not acceptable'
            # 자음일 경우
            if ((password[i] not in vowel) and (password[i+1] not in vowel) and (password[i+2] not in vowel)):
                return 'not acceptable'
            
        # 3. 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
        for i in range(0, len(password) - 1):
            # 연속으로 오는지 체크
            if password[i] == password[i+1]:
                if(not(password[i] == 'e' or password[i] == 'o')):
                    return 'not acceptable'
        return 'acceptable'
    else:
        return 'not acceptable'


while True:
    password = sys.stdin.readline().strip()
    if password == 'end': break
    pl = len(password)
    
    print("<"+password+">", "is", checkCondition()+'.')
    
    