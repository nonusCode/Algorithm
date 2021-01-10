import sys

sys.stdin = open("3499.퍼펙트셔플.txt", 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = input().split()

    if len(arr) % 2 == 0:
        res = arr[:len(arr)//2]
        tmp = arr[len(arr)//2:]
    else:
        res = arr[:len(arr)//2+1]
        tmp = arr[len(arr)//2+1:]

    cnt = 1
    for i in range(len(tmp)):
        res.insert(i+cnt, tmp[i])
        cnt += 1
    
    print(f"#{tc}", end=' ')
    print(*res)