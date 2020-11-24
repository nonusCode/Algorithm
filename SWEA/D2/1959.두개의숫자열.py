import sys

sys.stdin = open("1959.두개의숫자열.txt", 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        N, M = M, N
        A, B = B, A

    # 1
    res = []
    for i in range(M-N+1):
        tmp = []
        for j in range(N):
            tmp.append(A[j] * B[j+i])
        res.append(sum(tmp))
    
    # # 2
    # res = -1000000
    # for i in range(M-N+1):
    #     tmp = 0
    #     for j in range(N):
    #         tmp += A[j] * B[j+i]
    #     res = max(res, tmp)

    print(f"#{tc} {max(res)}")