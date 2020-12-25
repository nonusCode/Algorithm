import sys

sys.stdin = open("4406.모음이보이지않는사람.txt", 'r')

for tc in range(1, int(input())+1):
    S = input()

    sol = ['a', 'e', 'i', 'o', 'u']
    for i in sol:
        S = S.replace(i, '')
    
    print(f"#{tc} {S}")