import sys

sys.stdin = open("5549.홀수일까짝수일까.txt", 'r')

for tc in range(1, int(input())+1):
    N = int(input())

    if N % 2 != 0:
        print(f"#{tc} Odd")
    else:
        print(f"#{tc} Even")