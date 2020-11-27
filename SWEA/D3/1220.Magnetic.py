import sys

sys.stdin = open("1220.Magnetic.txt", 'r')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = 0
    for i in range(N):
        tmp = 0
        for j in range(N):
            if arr[j][i] == 0:
                continue
            if arr[j][i] == 1:
                tmp += 1
            if tmp > 0 and arr[j][i] == 2:
                tmp = 0
                res += 1
        
    print(f"#{tc} {res}")