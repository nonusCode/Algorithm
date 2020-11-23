import sys
import operator

sys.stdin = open("1204.최빈수구하기.txt", 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    res = dict()
    for i in arr:
        res[i] = arr.count(i)
    
    res = sorted(res.items(), key=operator.itemgetter(1), reverse=True)
    
    print(f"#{tc} {res[0][0]}")