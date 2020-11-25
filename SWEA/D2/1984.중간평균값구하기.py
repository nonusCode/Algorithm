import sys

sys.stdin = open("1984.중간평균값구하기.txt", 'r')

for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))

    arr.sort()
    print(f"#{tc} {round(sum(arr[1:-1]) / len(arr[1:-1]))}")