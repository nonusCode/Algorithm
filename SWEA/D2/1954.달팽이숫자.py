import sys

sys.stdin = open("1954.달팽이숫자.txt", 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    
    dx = [0, 1, 0, -1] # 우 하 좌 상
    dy = [1, 0, -1, 0]

    arr = [[0] * N for _ in range(N)]
    x, y = 0, 0
    cnt = 1
    while True:
        if arr[x][y] != 0:
            break
        arr[x][y] = cnt
        cnt += 1
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
                x = nx
                y = ny
                break
    
    print(f"#{tc}")
    for i in range(len(arr)):
        print(*arr[i])