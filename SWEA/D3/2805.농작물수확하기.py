import sys

sys.stdin = open("2805.농작물수확하기.txt", 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    
    mid = N // 2
    cnt = 0
    res = 0
    for i in range(N):
        for j in range(mid-cnt, mid+cnt+1):
            res += arr[i][j]
        if i < mid:
            cnt += 1
        else:
            cnt -= 1
    
    print(f"#{tc} {res}")