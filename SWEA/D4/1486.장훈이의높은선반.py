import sys

sys.stdin = open("1486.장훈이의높은선반.txt", 'r')

def powerSet(idx):
    global res
    if idx == N:
        tmp = 0
        for i in range(N):
            if check[i]:
                tmp += arr[i]
        if tmp >= B and (tmp - B) < res:
            res = tmp - B
        return
    check[idx] = 1
    powerSet(idx+1)
    check[idx] = 0
    powerSet(idx+1)

for tc in range(1, int(input())+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    check = [0] * N
    res = 100000
    powerSet(0)
    
    print(f"#{tc} {res}")