import sys

sys.stdin = open("3142.영준이와신비한뿔의숲.txt", 'r')

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())

    u = 2*m - n
    t = n - m
    
    print(f"#{tc} {u} {t}")