import sys

sys.stdin = open("5603.건초더미.txt", 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [int(input()) for _ in range(N)]

    sol = sum(arr) // N
    res = 0
    for i in arr:
        while True:
            if i == sol:
                break
            if i < sol:
                i += 1
                res += 1
            elif i > sol:
                i -= 1
                res += 1
   
    print(f"#{tc} {res // 2}")