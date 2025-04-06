import sys
import math
import time
start = time.time()
sys.stdin = open("[Testcase]_codetree-db_41.txt", "r")

db = dict()

Q = int(input())
for q in range(Q):
    i = list(input().split())
    c = i[0]
    if c == 'init':
        db = dict()
        continue
    elif c == 'insert':
        name, value = i[1], int(i[2])
        if name in db :
            print(0)
        elif value in db.values():
            print(0)
        else :
            db[name] = value
            print(1)
        continue
    elif c == 'delete':
        name = i[1]
        if name not in db:
            print(0)
        else :
            print(db[name])
            del(db[name])
        continue
    elif c == 'rank':
        k = int(i[1])
        t = list(db.values())
        if len(t) < k :
            print("None")
            continue
        t.sort()
        thing = t[k-1]
        
        for i in db.keys():
            if db[i] == thing:
                print(i)
                break
        continue
    elif c == 'sum':
        k = int(i[1])
        t = list(db.values())
        t.sort()
        res = 0
        for i in t:
            if i <= k :
                res += i
            else :
                break
        print(res)
end = time.time()
print(f"{end-start:.5f} sec")