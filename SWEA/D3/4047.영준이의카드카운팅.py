import sys

sys.stdin = open("4047.영준이의카드카운팅.txt", 'r')

for tc in range(1, int(input())+1):
    S = input()

    sol = []
    s = 0
    d = 0
    h = 0
    c = 0
    res = True
    for i in range(0, len(S), 3):
        sol.append(S[i:i+3])
    # 같은 카드 확인
    for i in range(len(sol)):
        for j in range(i+1, len(sol)):
            if sol[i] == sol[j]:
                res = False
    # 가지고 있는 카드 개수
    for i in range(len(sol)):
        if sol[i][0] == 'S':
            s += 1
        elif sol[i][0] == 'D':
            d += 1
        elif sol[i][0] == 'H':
            h += 1
        elif sol[i][0] == 'C':
            c += 1
    
    if res:
        print(f"#{tc} {13-s} {13-d} {13-h} {13-c}")
    else:
        print(f"#{tc} ERROR")