import sys

sys.stdin = open("10505.소득불균형.txt", 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))

    res = 0
    for i in arr:
        if i <= sum(arr) // N:
            res += 1
    
    print(f"#{tc} {res}")