import sys

sys.stdin = open("10580.전봇대.txt", 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = 0
    for i in range(N):
        for j in range(i+1, N):
            if arr[i][0] < arr[j][0] and arr[i][1] > arr[j][1]:
                res += 1
            elif arr[i][0] > arr[j][0] and arr[i][1] < arr[j][1]:
                res += 1

    print(f"#{tc} {res}")