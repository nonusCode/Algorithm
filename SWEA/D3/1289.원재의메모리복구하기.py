import sys

sys.stdin = open("1289.원재의메모리복구하기.txt", 'r')

for tc in range(1, int(input())+1):
    S = input()

    cnt = 0
    if S[0] != '0':
        cnt = 1
    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            cnt += 1
    
    print(f"#{tc} {cnt}")