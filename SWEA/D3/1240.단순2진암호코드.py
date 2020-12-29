import sys

sys.stdin = open("1240.단순2진암호코드.txt", 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    sol = {"0001101": 0, "0011001": 1, "0010011": 2, "0111101": 3, "0100011": 4, "0110001": 5, "0101111": 6, "0111011": 7, "0110111": 8, "0001011": 9}
    tmp = ''
    for i in range(len(arr)):
        for j in range(len(arr[i])-1, -1, -1):
            if arr[i][j] == '1':
                tmp = arr[i][j-55:j+1]
                break

    res = []
    for i in range(0, len(tmp), 7):
        res.append(int(sol[tmp[i:i+7]]))
    
    if ((res[0] + res[2] + res[4] + res[6]) * 3 + res[1] + res[3] + res[5] + res[7]) % 10 == 0:
        print(f"#{tc} {sum(res)}")
    else:
        print(f"#{tc} 0")