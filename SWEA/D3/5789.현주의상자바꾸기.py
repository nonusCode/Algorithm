import sys

sys.stdin = open("5789.현주의상자바꾸기.txt", 'r')

for tc in range(1, int(input())+1):
    N, Q = map(int, input().split())

    res = [0] * N
    cnt = 1
    for i in range(Q):
        L, R = map(int, input().split())
        
        for j in range(L, R+1):
            res[j-1] = cnt
        cnt += 1
    
    print(f"#{tc}", end=' ')
    print(*res)