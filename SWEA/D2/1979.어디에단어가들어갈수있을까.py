import sys

sys.stdin = open("1979.어디에단어가들어갈수있을까.txt", 'r')

# 1
for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    res = 0
    for i in range(N):
        c_cnt = 0
        r_cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                c_cnt += 1
            else:
                if c_cnt == K:
                    res += 1
                c_cnt = 0
          
            if arr[j][i] == 1:
                r_cnt += 1
            else:
                if r_cnt == K:
                    res += 1
                r_cnt = 0


        if c_cnt == K:
            res += 1
        if r_cnt == K:
            res += 1

# # 2
# for tc in range(1, int(input()) + 1):
#     N, K = map(int, input().split())
#     arr = [input().split() for _ in range(N)]
#     arr2 = list(zip(*arr))

#     res = 0
#     for i in range(N):
#         res += ''.join(arr[i]).split('0').count('1' * K)
#         res += ''.join(arr2[i]).split('0').count('1' * K)
    
    print(f"#{tc} {res}")