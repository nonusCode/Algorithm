import sys

sys.stdin = open("6190.정곤이의단조증가하는수.txt", 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))

    res = -1
    for i in range(N-1):
        for j in range(i+1, N):
            tmp = arr[i] * arr[j]
            o = tmp
            prev = 10
            sol = True
            while tmp:
                q = tmp % 10
                tmp = tmp // 10
                if prev < q:
                    sol = False
                    break
                prev = q
            if sol and o > res:
                res = o
    
    print(f"#{tc} {res}")