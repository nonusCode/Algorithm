import sys

sys.stdin = open("3408.세가지합구하기.txt", 'r')

for tc in range(1, int(input())+1):
    N = int(input())

    S1 = N*(N+1) // 2
    S2 = N ** 2
    S3 = N * (N+1)
    
    print(f"#{tc} {S1} {S2} {S3}")