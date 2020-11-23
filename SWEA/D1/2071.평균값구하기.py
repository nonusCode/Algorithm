import sys

sys.stdin = open("2071.평균값구하기.txt", 'r')

for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    
    tmp = 0
    for i in arr:
        tmp += i
        res = round(tmp / 10)
    
    print(f"#{tc} {res}")