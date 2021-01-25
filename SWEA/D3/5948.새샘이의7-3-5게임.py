import sys
from itertools import combinations

sys.stdin = open("5948.새샘이의7-3-5게임.txt", 'r')

for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))

    sol = []
    for i in range(len(arr)+1):
        tmp = combinations(arr, i)
        sol.extend(tmp)

    res = set()
    for i in sol:
        if len(i) == 3:
            res.add(sum(i)) 
    res = sorted(list(res), reverse=True)

    print(f"#{tc} {res[4]}")