import sys

sys.stdin = open("11387.몬스터사냥.txt", 'r')

for tc in range(1, int(input())+1):
    D, L, N = map(int, input().split())
    
    res = D
    for i in range(2, N+1):
        res += D*(1+(i-1)*L/100)

    print(f"#{tc} {int(res)}")