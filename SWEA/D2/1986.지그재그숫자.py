import sys

sys.stdin = open("1986.지그재그숫자.txt", 'r')

for tc in range(1, int(input())+1):
    N = int(input())

    res = 0
    for i in range(1, N+1):
        if i % 2 != 0:
           res += i
        else:
            res -= i
        
    print(f"#{tc} {res}")