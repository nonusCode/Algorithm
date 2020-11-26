import sys

sys.stdin = open("1206.View.txt", 'r')

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    res = 0
    for i in range(2, N-2):
        sol = max(arr[i-2], arr[i-1], arr[i+1], arr[i+2])
        if sol < arr[i]:
            res += arr[i]-sol
    
    print(f"#{tc} {res}")