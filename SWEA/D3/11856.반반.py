import sys

sys.stdin = open("11856.반반.txt", 'r')

for tc in range(1, int(input())+1):
    S = input()
    
    sol = dict()
    res = True
    for i in S:
        sol[i] = S.count(i)
    
    for i, v in sol.items():
        if v == 2:
            pass
        else:
            res = False
    
    if res:
        print(f"#{tc} Yes")
    else:
        print(f"#{tc} No")