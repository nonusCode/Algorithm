import sys

sys.stdin = open("10200.구독자전쟁.txt", 'r')

for tc in range(1, int(input())+1):
    N, A, B = map(int, input().split())
    
    print(f"#{tc} {min(A, B)} {max(A+B-N, 0)}")