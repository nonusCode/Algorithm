import sys

sys.stdin = open("2072.홀수만더하기.txt", 'r')

for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    
    res = 0
    for i in arr:
        if i % 2 != 0:
            res += i
    
    print(f"#{tc} {res}")