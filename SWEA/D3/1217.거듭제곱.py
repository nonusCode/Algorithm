import sys

sys.stdin = open("1217.거듭제곱.txt", 'r')

def power(N, M, res):
    if M == 0:
        return f"#{tc} {res}"
    res *= N
    return power(N, M-1, res)

for t in range(1, 11):
    tc = int(input())
    N, M = map(int, input().split())
    
    print(power(N, M, 1))