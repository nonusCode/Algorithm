import sys

sys.stdin = open("2806.N-Queen.txt", 'r')

def nQueen(x):
    global cnt
    # x : queen이 놓을 수 있는 자리 확인
    # 놓을 수 있으면 영향을 미치는 모든 칸에 표시
    if x == N: # N개의 queen을 모두 놓음
        cnt += 1
        return
    
    for i in range(N):
        if check[x][i] == 0:
            marking(x, i)
            nQueen(x+1)
            unMarking(x, i)

def marking(x, y):
    # 12시부터 시계방향
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]
        while True:
            if 0 <= nx < N and 0 <= ny < N:
                check[nx][ny] += 1
                nx += dx[d]
                ny += dy[d]
            else:
                break

def unMarking(x, y):
    # 12시부터 시계방향
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]
        while True:
            if 0 <= nx < N and 0 <= ny < N:
                check[nx][ny] -= 1
                nx += dx[d]
                ny += dy[d]
            else:
                break

for tc in range(1, int(input())+1):
    N = int(input())
    
    check = [[0] * N for _ in range(N)]
    cnt = 0
    nQueen(0)

    print(f"#{tc} {cnt}")