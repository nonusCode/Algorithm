import sys

sys.stdin = open("1265.달란트2.txt", 'r')

for tc in range(1, int(input())+1):
    N, P = map(int, input().split())
    
    q = N // P
    r = N % P
    
    print(f"#{tc} {pow(q, (P-r)) * pow(q+1, r)}")