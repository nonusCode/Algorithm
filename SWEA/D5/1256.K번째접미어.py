import sys

sys.stdin = open("1256.K번째접미어.txt", 'r')

for tc in range(1, int(input())+1):
    K = int(input())
    S = input()

    res = []
    for i in range(len(S)):
        res.append(S[i:])

    print(f"#{tc} {sorted(res)[K-1]}")