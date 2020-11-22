import sys

sys.stdin = open("1545.거꾸로출력해보아요.txt", 'r')

N = int(input())

for i in range(N, -1, -1):
    print(i, end=' ')