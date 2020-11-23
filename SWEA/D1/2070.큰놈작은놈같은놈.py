import sys

sys.stdin = open("2070.큰놈작은놈같은놈.txt", 'r')

for tc in range(1, int(input())+1):
    a, b = map(int, input().split())

    if a > b:
        res = '>'
    elif a == b:
        res = '='
    else:
        res = '<'
    
    print(f"#{tc} {res}")