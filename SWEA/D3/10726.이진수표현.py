import sys

sys.stdin = open("10726.이진수표현.txt", 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    res = True
    for i in range(N):
        if not M % 2:
            res = False
        M //= 2
    
    if res:
        print(f"#{tc} ON")
    else:
        print(f"#{tc} OFF")