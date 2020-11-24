import sys

sys.stdin = open("1945.간단한소인수분해.txt", 'r')

for tc in range(1, int(input())+1):
    N = int(input())

    res = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}
    for k, v in res.items():
        while N % k == 0:
            N //= k
            res[k] += 1

    print(f"#{tc}", end=' ')
    print(*res.values())