import sys

sys.stdin = open("1226.미로1.txt", 'r')

for t in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]

    dx = [-1, 1, 0, 0] # 상 하 우 좌
    dy = [0, 0, 1, -1]

    v = [[0]*16 for _ in range(16)]
    stack = []
    res = False
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                stack.append((i, j))
                v[i][j] = 1
                while len(stack):
                    x, y = stack.pop()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < 16 and 0 <= ny < 16 and arr[nx][ny] != 1 and v[nx][ny] == 0:
                            stack.append((nx, ny))
                            v[nx][ny] = 1
                            if arr[nx][ny] == 3:
                                res = True
                                break
    
    if res:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")