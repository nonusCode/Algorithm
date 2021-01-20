import sys

sys.stdin = open("3260.두수의덧셈.txt", 'r')

for tc in range(1, int(input())+1):
    A, B = map(int, input().split())

    print(f"#{tc} {A+B}")