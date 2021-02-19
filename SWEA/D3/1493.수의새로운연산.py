import sys

sys.stdin = open("1493.수의새로운연산.txt", 'r')

for tc in range(1, int(input())+1):
    p, q = map(int, input().split())

    sol = []
    for i in range(1, 300):
        for j in range(1, i+1):
            sol.append((j, i-j+1))
    res = sol.index((sol[p-1][0] + sol[q-1][0], sol[p-1][1] + sol[q-1][1]))+1

    print(f"#{tc} {res}")