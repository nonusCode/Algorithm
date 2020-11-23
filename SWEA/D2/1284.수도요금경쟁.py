import sys

sys.stdin = open("1284.수도요금경쟁.txt", 'r')

for tc in range(1, int(input())+1):
    P, Q, R, S, W = map(int, input().split())

    A = P * W
    if W <= R:
        B = Q
    else:
        B = Q + ((W-R) * S)
    
    print(f"#{tc} {min(A, B)}")