import sys

sys.stdin = open("1221.계산기1.txt", 'r')

for tc in range(1, 11):
    N = int(input())
    res = sum(map(int, input().split('+')))

    print(f"#{tc} {res}")