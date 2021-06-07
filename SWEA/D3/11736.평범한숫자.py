import sys

sys.stdin = open("11736.평범한숫자.txt", 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    P = list(map(int, input().split()))

    res = 0
    for i in range(N-2):
        if (P[i+1]-P[i]) * (P[i+1]-P[i+2]) < 0:
            res += 1
    
    print(f"#{tc} {res}")