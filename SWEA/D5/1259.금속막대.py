import sys

sys.stdin = open("1259.금속막대.txt", 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))

    tmp = []
    for i in range(len(arr)//2):
        tmp.append(arr[2*i:2*i+2])
    res = [tmp.pop(0)]

    while True:
        if len(tmp) == 1:
            break
        for i in range(len(tmp)):
            if res[-1][1] == tmp[i][0]:
                res.append(tmp[i])
                tmp.remove(tmp[i])
                break
            elif res[0][0] == tmp[i][1]:
                res.insert(0, tmp[i])
                tmp.remove(tmp[i])
                break
        
    if res[-1][1] == tmp[0][0]:
        res.append(tmp[0])
        tmp.remove(tmp[0])
    elif res[0][0] == tmp[0][1]:
        res.insert(0, tmp[0])
        tmp.remove(tmp[0])
    
    print(f"#{tc}", end=' ')
    for i in range(len(res)):
        for j in range(len(res[i])):
            print(res[i][j], end=' ')
    print()

