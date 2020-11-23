import sys

sys.stdin = open("1926.간단한369게임.txt", 'r')

N = int(input())

for i in range(1, N+1):
    res = 0
    res += str(i).count('3')
    res += str(i).count('6')
    res += str(i).count('9')

    if res > 0:
        print('-' * res, end=' ')
    else:
        print(i, end=' ')