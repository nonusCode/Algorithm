import sys

sys.stdin = open("10804.문자열의거울상.txt", 'r')

for tc in range(1, int(input())+1):
    S = input()
    
    res = ''
    for i in range(len(S)-1, -1, -1):
        if S[i] == 'b':
            res += 'd'
        elif S[i] == 'd':
            res += 'b'
        elif S[i] == 'p':
            res += 'q'
        else:
            res += 'p'

    print(f"#{tc} {res}")