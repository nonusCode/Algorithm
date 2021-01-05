import sys

sys.stdin = open("5162.두가지빵의딜레마.txt", 'r')

for tc in range(1, int(input())+1):
    A, B, C = map(int, input().split())

    res = C // min(A, B)
    
    print(f"#{tc} {res}")