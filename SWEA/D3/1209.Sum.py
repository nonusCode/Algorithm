import sys

sys.stdin = open("1209.Sum.txt", 'r')

for t in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    
    res = 0
    for i in range(len(arr)):
        c_sum = 0
        r_sum = 0
        for j in range(len(arr)):
            c_sum += arr[i][j]
            r_sum += arr[j][i]
        if res < max(c_sum, r_sum):
            res = max(c_sum, r_sum)
    
    d_sum = 0
    rd_sum = 0
    for i in range(len(arr)):
        d_sum += arr[i][i]
        rd_sum += arr[i][len(arr)-i-1]
    if res < max(d_sum, rd_sum):
        res = max(d_sum, rd_sum)

    print(f"#{tc} {res}")