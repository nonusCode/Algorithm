import sys

sys.stdin = open("3314.보충학습과평균.txt", 'r')

for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))

    res = 0
    for i in arr:
        if i < 40:
            res += 40
        else:
            res += i
            
    print(f"#{tc} {res//len(arr)}")