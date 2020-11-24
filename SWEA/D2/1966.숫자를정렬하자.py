import sys

sys.stdin = open("1966.숫자를정렬하자.txt", 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    print(f"#{tc}", end=' ')
    print(*arr)