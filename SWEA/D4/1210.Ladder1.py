import sys

sys.stdin = open("1210.Ladder1.txt", 'r')

for t in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    dx = [0, 0, 1] # 좌 우 하
    dy = [-1, 1, 0]

    res = 0
    for i in range(100):
        if arr[0][i] == 1:
            v = [[0]*(100) for _ in range(100)]
            stack = []
            stack.append((0, i))
            v[0][i] = 1
            while len(stack):
                x, y = stack.pop()
                for d in range(3):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < 100 and 0 <= ny < 100 and v[nx][ny] == 0:
                        if arr[nx][ny] == 1:
                            stack.append((nx, ny))
                            v[nx][ny] = 1
                            break
                        elif arr[nx][ny] == 2:
                            res = i
                            
    print(f"#{tc} {res}")