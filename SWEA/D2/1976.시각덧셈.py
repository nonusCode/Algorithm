import sys

sys.stdin = open("1976.시각덧셈.txt", 'r')

for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))

    h = arr[0] + arr[2] # hour
    m = arr[1] + arr[3] # minute
    if h > 12:
        h = h - 12
    if m > 60:
        h = h + 1
        m = m - 60

    print(f"#{tc} {h} {m}")