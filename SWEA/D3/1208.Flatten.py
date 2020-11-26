import sys

sys.stdin = open("1208.Flatten.txt", 'r')

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    
    arr.sort()
    res = 0
    for i in range(N):
        arr[-1] -= 1
        arr[0] += 1
        arr.sort()
    res = arr[-1] - arr[0]
    
    print(f"#{tc} {res}")