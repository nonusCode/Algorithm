import sys

sys.stdin = open("1946.간단한압축풀기.txt", 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    res = ''
    for i in range(N):
        C, K = input().split()
        
        res += C * int(K)
    print(f"#{tc}")
    # 1
    for i in range(0, len(res), 10):
        print(res[i:i+10])

    # # 2
    # cnt = 1
    # for i in res:
    #     print(i, end='')
    #     if cnt % 10 == 0:
    #         print()
    #     cnt += 1
    # print()