import sys

sys.stdin = open("9700.USB꽂기의미스터리.txt", 'r')

for tc in range(1, int(input())+1):
    p, q = map(float, input().split())

    s1 = (1-p) * q
    s2 = p * (1-q) * q

    if s1 < s2:
        print(f"#{tc} YES")
    else:
        print(f"#{tc} NO")