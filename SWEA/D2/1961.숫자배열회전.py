import sys

sys.stdin = open("1961.숫자배열회전.txt", 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()) for _ in range(N))

    res_1 = list(zip(*arr[::-1]))
    res_2 = list(zip(*res_1[::-1]))
    res_3 = list(zip(*res_2[::-1]))

    print(f"#{tc}")
    for i in range(N):
        for j in range(N):
            print(res_1[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(res_2[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(res_3[i][j], end='')
        print()