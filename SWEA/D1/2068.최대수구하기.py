import sys

sys.stdin = open("2068.최대수구하기.txt", 'r')

for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    
    print(f"#{tc} {max(arr)}")