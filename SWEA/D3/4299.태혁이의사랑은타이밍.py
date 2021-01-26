import sys

sys.stdin = open("4299.태혁이의사랑은타이밍.txt", 'r')

for tc in range(1, int(input())+1):
    D, H, M = map(int, input().split())

    res = 0
    if D > 11:
        D = D - 11
        H = H - 11
        M = M - 11
        res = (D*24+H)*60 + M
    elif D <= 11:
        if H >= 11:
            H = H - 11
            M = M - 11
            res = (H*60) + M
        elif H < 11:
            res = -1

    print(f"#{tc} {res}")