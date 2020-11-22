import sys

sys.stdin = open("1933.간단한N의약수.txt", 'r')

N = int(input())

for i in range(1, N+1):
    if N % i == 0:
        print(i, end=' ')