import sys

sys.stdin = open("1213.String.txt", 'r', encoding='UTF8')

for tc in range(1, 11):
    N = int(input())
    S = input()
    data = input()

    cnt = 0
    for i in range(len(data)):
        if data[i:len(S)+i] == S:
            cnt += 1

    print(f"#{tc} {cnt}")