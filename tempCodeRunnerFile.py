확인
            for r in range(fe+1-L, fe+1):
                if r in h :
                    print('이미 설치됨: h, r', h, r)
                    return False
            # 설치
            for r in range(fe+1-L, fe+1):
                h.append(r)
                tl[r] += 1
                print('경사