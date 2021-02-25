import sys
from itertools import combinations

sys.stdin = open("2817.부분수열의합.txt", 'r')

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    res = 0
    for i in range(1, N+1):
        tmp = combinations(arr, i)
        for j in tmp:
            if sum(j) == K:
                res += 1
    
    print(f"#{tc} {res}")