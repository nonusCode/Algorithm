import sys

sys.stdin = open("3456.직사각형길이찾기.txt", 'r')

for tc in range(1, int(input())+1):
    a, b, c = map(int, input().split())

    res = 0
    if a == b:
        res = c
    elif a == c:
        res = b
    else:
        res = a

    print(f"#{tc} {res}")