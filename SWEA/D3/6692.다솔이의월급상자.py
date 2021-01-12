import sys

sys.stdin = open("6692.다솔이의월급상자.txt", 'r')

for tc in range(1, int(input())+1):
    N = int(input())

    res = 0
    for i in range(N):
        arr = input().split()

        p = float(arr[0])
        x = int(arr[1])
        res += p*x

    print(f"#{tc} {res}")