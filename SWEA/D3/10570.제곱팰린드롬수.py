import sys

sys.stdin = open("10570.제곱팰린드롬수.txt", 'r')

for tc in range(1, int(input())+1):
    A, B = map(int, input().split())

    res = 0
    for i in range(A, B+1):
        if str(round((i**0.5), 2))[-1] == '0':
            if str(i) == str(i)[::-1] and str(int(i**0.5)) == str(int(i**0.5))[::-1]:
                res += 1
    
    print(f"#{tc} {res}")