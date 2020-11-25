import sys

sys.stdin = open("2005.파스칼의삼각형.txt", 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    
    res = [[0] * N for _ in range(N)]
    res[0][0] = 1
    
    print(f"#{tc}")
    print(res[0][0])
    
    for i in range(1, N):
        for j in range(0, i+1):
            res[i][j] = res[i-1][j-1] + res[i-1][j]
            print(res[i][j], end=' ')
        print()