import sys

sys.stdin = open("1859.백만장자프로젝트.txt", 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))

    tmp = arr[-1]
    res = 0
    for i in range(len(arr)-1, 0, -1):
        if tmp > arr[i-1]:
            res += tmp - arr[i-1]
        else:
            tmp = arr[i-1]
    
    print(f"#{tc} {res}")