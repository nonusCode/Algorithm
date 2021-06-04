import sys

sys.stdin = open("11445.무한사전.txt", 'r')

for tc in range(1, int(input())+1):
    P = input().strip()
    Q = input().strip()

    if P + 'a' != Q:
        print(f"#{tc} Y")
    else:
        print(f"#{tc} N")