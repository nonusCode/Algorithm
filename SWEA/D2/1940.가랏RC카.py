import sys

sys.stdin = open("1940.가랏RC카.txt", 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    d = 0 # distance
    s = 0 # speed
    for i in range(N):
        if arr[i][0] == 1:
            s += arr[i][1]
            d += s
        elif arr[i][0] == 2:
            if s == 0:
                s += 0
                d += s
            else:
                s -= arr[i][1]
                d += s
        else:
            d += s
    
    print(f"#{tc} {d}")