import sys

sys.stdin = open("2001.파리퇴치.txt", 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    res = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            tmp = 0
            for k in range(M):
                for l in range(M):
                    tmp += arr[i+k][j+l]
                if res < tmp:
                    res = tmp

    print(f"#{tc} {res}")