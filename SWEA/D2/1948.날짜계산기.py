import sys

sys.stdin = open("1948.날짜계산기.txt", 'r')

for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))

    sol = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    tmp = arr[2] - arr[0]
    res = 0
    if arr[0] < arr[2]:
        for i in range(tmp):
            res += sol[arr[0]+i]
        res += (arr[3]-arr[1]) + 1
    else:
        res += (arr[3]-arr[1]) + 1
    
    print(f"#{tc} {res}")