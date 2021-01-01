import sys

sys.stdin = open("5431.민석이의과제체크하기.txt", 'r')

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    
    res = [0] * (N+1)
    for i in arr:
        res[i] = 1
    
    print(f"#{tc}", end=' ')
    for i, v in enumerate(res):
        if i != 0 and v == 0:
            print(f"{i}", end=' ')
    print()