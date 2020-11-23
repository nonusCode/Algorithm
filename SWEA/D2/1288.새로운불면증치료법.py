import sys

sys.stdin = open("1288.새로운불면증치료법.txt", 'r')

for tc in range(1, int(input())+1):
    N = int(input())

    res = [0] * 10
    cnt = 1
    while sum(res) < 10:
        tmp = N
        tmp *= cnt
        for i in str(tmp):
            if res[int(i)] == 0:
                res[int(i)] = 1
        cnt += 1
    
    print(f"#{tc} {(cnt-1) * N}")