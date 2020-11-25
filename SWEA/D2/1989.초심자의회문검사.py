import sys

sys.stdin = open("1989.초심자의회문검사.txt", 'r')

for tc in range(1, int(input())+1):
    S = input()
    
    res = 0
    if S == S[::-1]:
        res = 1

    print(f"#{tc} {res}")