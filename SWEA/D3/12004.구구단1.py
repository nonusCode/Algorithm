import sys

sys.stdin = open("12004.구구단1.txt", 'r')

for tc in range(1, int(input())+1):
    N = int(input())

    res = False
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == N:
                res = True

    if res:
        print(f"#{tc} Yes")
    else:
        print(f"#{tc} No")