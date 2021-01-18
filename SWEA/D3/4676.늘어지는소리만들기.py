import sys

sys.stdin = open("4676.늘어지는소리만들기.txt", 'r')

for tc in range(1, int(input())+1):
    S = list(input())
    H = int(input())
    arr = list(sorted(map(int, input().split()), reverse=True))
    
    for i in arr:
        S.insert(i, '-')
    
    print(f"#{tc} {''.join(map(str, S))}")