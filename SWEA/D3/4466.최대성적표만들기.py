import sys

sys.stdin = open("4466.최대성적표만들기.txt", 'r')

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()
    res = 0
    for i in range(K):
        res += arr.pop()
    
    print(f"#{tc} {res}")