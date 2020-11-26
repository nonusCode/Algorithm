import sys

sys.stdin = open("1215.회문1.txt", 'r')

for tc in range(1, 11):
    N = int(input())
    arr = [list(input()) for _ in range(8)]
    
    res = 0
    arr_1 = list(zip(*arr[::-1]))
    for i in range(len(arr)):
        for j in range(len(arr)-N+1):
            c_tmp = arr[i][j:N+j] 
            r_tmp = arr_1[i][j:N+j]
            if c_tmp == c_tmp[::-1]:
                res += 1
            if r_tmp == r_tmp[::-1]:
                res += 1

    print(f"#{tc} {res}")