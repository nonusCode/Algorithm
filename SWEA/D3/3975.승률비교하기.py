import sys

sys.stdin = open("3975.승률비교하기.txt", 'r')

res = []
for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))

    a = arr[0] / arr[1]
    b = arr[2] / arr[3]
    if a > b:
        res.append(f"#{tc} ALICE")
    elif a < b:
        res.append(f"#{tc} BOB")
    else:
        res.append(f"#{tc} DRAW")

print('\n'.join(res))