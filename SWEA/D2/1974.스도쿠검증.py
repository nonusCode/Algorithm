import sys

sys.stdin = open("1974.스도쿠검증.txt", 'r')

for tc in range(1, int(input())+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    res = 1
    for i in range(9):
        c_check = [0] * 10
        r_check = [0] * 10
        for j in range(9):
            if c_check[arr[i][j]] != 0:
                res = 0
                break
            if r_check[arr[j][i]] != 0:
                res = 0
                break
            c_check[arr[i][j]] = 1
            r_check[arr[j][i]] = 1

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            s_check = [0] * 10
            for k in range(i, i+3):
                for l in range(j, j+3):
                    if s_check[arr[k][l]] != 0:
                        res = 0
                        break
                    s_check[arr[k][l]] = 1

    print(f"#{tc} {res}")