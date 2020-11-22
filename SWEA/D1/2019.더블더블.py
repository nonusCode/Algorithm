import sys

sys.stdin = open("2019.더블더블.txt", 'r')

N = int(input())

res = 1
for i in range(N+1):
    print(res, end=' ')
    res = res*2