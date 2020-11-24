import sys

sys.stdin = open("1970.쉬운거스름돈.txt", 'r')

for tc in range(1, int(input())+1):
    N = int(input())

    sol = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    res = [0] * len(sol)

    tmp = N
    for i in range(len(sol)):
        if sol[i] <= tmp:
            res[i] = tmp // sol[i]
            tmp = tmp % sol[i]
    
    print(f"#{tc}")
    print(*res)